import type { Plugin } from "@opencode-ai/plugin"
import { spawnSync } from "node:child_process"
import { join } from "node:path"

// Par del hook Stop de Claude Code (`.claude/hooks/validar_backlog.sh`). Cuando la sesión
// queda inactiva, corre ese mismo script (`regenerar.py --check`). Si el plan tiene
// errores, se los manda al agente como un mensaje nuevo para que los corrija antes de
// cerrar. Hay como máximo 2 reintentos seguidos por sesión, para no entrar en un bucle si
// el agente no puede arreglarlo. Las subsesiones (subagentes) no se revisan, porque las
// revisa la sesión principal cuando termina.

const MAX_REINTENTOS = 2

export const ValidarBacklogPlugin: Plugin = async ({ client, directory }) => {
  const root = directory ?? process.cwd()
  const script = join(root, ".claude", "hooks", "validar_backlog.sh")
  const reintentos = new Map<string, number>()

  return {
    event: async ({ event }) => {
      if (event.type !== "session.idle") return
      const sessionID = event.properties.sessionID

      const sesion = await client.session.get({ path: { id: sessionID } })
      if (sesion.data?.parentID) return

      const result = spawnSync("bash", [script], {
        cwd: root,
        env: { ...process.env, CLAUDE_PROJECT_DIR: root },
        encoding: "utf8",
        timeout: 60_000,
      })
      // El script sale con 2 solo cuando el plan tiene inconsistencias.
      if (result.status !== 2) {
        reintentos.delete(sessionID)
        return
      }
      const n = (reintentos.get(sessionID) ?? 0) + 1
      reintentos.set(sessionID, n)
      if (n > MAX_REINTENTOS) return

      await client.session.promptAsync({
        path: { id: sessionID },
        body: { parts: [{ type: "text", text: result.stderr.trim() }] },
      })
    },
  }
}
