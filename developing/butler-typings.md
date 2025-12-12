# Butler TypeScript Typings

The itch app communicates with [butler](https://github.com/itchio/butler) via a JSON-RPC interface. Butler's API is defined in Go, and TypeScript type definitions are generated from this specification using a tool called `generous`.

## How It Works

Butler's API messages (requests, responses, and notifications) are defined in Go structs within the butler repository. The `generous` tool reads these definitions and generates corresponding TypeScript types and request creators that work with the `@itchio/butlerd` package.

The generated file lives at `src/common/butlerd/messages.ts` in the itch repository.

## Synchronizing Typings

When butler's API changes, the TypeScript typings in itch need to be regenerated to match. This ensures type safety when making butler calls from the app.

To regenerate the typings, ensure you have the butler repository checked out alongside itch:

```
parent/
├── butler/
└── itch/
```

Then run:

```bash
npm run sync-butler
```

This runs the generous generator from the butler repo and outputs the updated TypeScript definitions.

## When to Sync

You should regenerate the typings when:

- Butler adds new API endpoints
- Butler modifies existing request/response types
- Butler adds or changes notifications
- You're working with a newer version of butler that has API changes
