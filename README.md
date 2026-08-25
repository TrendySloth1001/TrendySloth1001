<img src="./header.svg" width="100%" alt="Nikhil Binwal" />

Fourth-year CSE student, specialising in AI/ML.

I'm drawn to the problems that start out as edge cases and quietly turn into the
whole problem. A lot of my time goes into rethinking the flow a user actually
takes through a product rather than the one we assumed they'd take, and into
writing code that stays reasonable as it grows.

---

### Currently building

**[shopxy](https://github.com/TrendySloth1001/shopxy)** — a commerce and invoicing
platform built as three surfaces over one backend:

- a **merchant** app for inventory, invoices, parties and vendors
- a **customer** companion app showing invitations and per-shop invoice ledgers
- a shared **Express + Prisma + Postgres** backend, with the same JWT shape across
  both apps so one account works in either

Both clients are Flutter, with web and desktop builds alongside mobile. The stack
runs on Docker Compose — Postgres, Redis and MinIO — and the interesting parts have
been the account-linking model between merchants and customers, POS payment flows,
and keeping the accounting side auditable.

---

### Technologies

**Languages and frameworks**

<table>
<tr>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/typescript" width="38" height="38" alt="" /><br /><sub>TypeScript</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/dart" width="38" height="38" alt="" /><br /><sub>Dart</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/flutter" width="38" height="38" alt="" /><br /><sub>Flutter</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/react" width="38" height="38" alt="" /><br /><sub>React</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/nodedotjs" width="38" height="38" alt="" /><br /><sub>Node.js</sub></td>
<td align="center" width="95">
<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/express/FFFFFF" /><img src="https://cdn.simpleicons.org/express" width="38" height="38" alt="" /></picture>
<br /><sub>Express</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/python" width="38" height="38" alt="" /><br /><sub>Python</sub></td>
</tr>
</table>

**Data and queues**

<table>
<tr>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/postgresql" width="38" height="38" alt="" /><br /><sub>PostgreSQL</sub></td>
<td align="center" width="95">
<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/prisma/A9B4C4" /><img src="https://cdn.simpleicons.org/prisma" width="38" height="38" alt="" /></picture>
<br /><sub>Prisma</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/redis" width="38" height="38" alt="" /><br /><sub>Redis</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/redis/A0A6AD" width="38" height="38" alt="" /><br /><sub>BullMQ</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/minio" width="38" height="38" alt="" /><br /><sub>MinIO</sub></td>
</tr>
</table>

**Infrastructure and hosting**

<table>
<tr>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/docker" width="38" height="38" alt="" /><br /><sub>Docker</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/nginx" width="38" height="38" alt="" /><br /><sub>Nginx</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/coolify" width="38" height="38" alt="" /><br /><sub>Coolify</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/cloudflare" width="38" height="38" alt="" /><br /><sub>Cloudflare</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/gnubash" width="38" height="38" alt="" /><br /><sub>SSH</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/linux" width="38" height="38" alt="" /><br /><sub>Linux</sub></td>
<td align="center" width="95"><img src="https://cdn.simpleicons.org/git" width="38" height="38" alt="" /><br /><sub>Git</sub></td>
</tr>
</table>

<sub>Deploys go out through Coolify, with Cloudflare Tunnels and plain SSH doing the reaching-in. BullMQ and SSH have no official brand mark, so they borrow the Redis and shell icons above.</sub>
