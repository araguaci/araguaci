"""Lista os repositórios públicos de araguaci na lista GitHub "My stack".

Repositórios privados e forks de terceiros ficam de fora.
Exige o GitHub CLI autenticado (`gh auth status`).
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date

LIST_NAME = "🚀 My stack"
OWNER = "araguaci"
EXCLUDE = {"araguaci"}

GROUPS: list[tuple[str, tuple[str, ...]]] = [
    (
        "Investigação e Brasil",
        (
            "lawfare",
            "abuso",
            "patria",
            "brasil-pela",
            "sabor-brazil",
            "observatorio",
            "jusmonitor",
            "vitimas",
            "republica",
            "odragao",
            "serie-demografica",
            "twitterfiles",
            "geoengineering",
            "gilmarmometro",
            "futuroroubado",
            "malvado",
            "taxad",
            "cronologia",
            "lockdowns",
            "ong-no-brasil",
            "sereis-como",
            "partido-das",
            "drogavermelha",
            "ponerologia",
            "mentes-perigosas",
            "satiagraha",
            "esperanca",
            "supremos-erros",
            "cronograma",
            "darknetwork",
            "guerra-da",
            "hatevaom",
            "brasileiros",
            "o-apagar",
            "os-5-carteis",
            "timeline-biowar",
        ),
    ),
    (
        "Fé e contemplação",
        (
            "catequese",
            "crux-sacra",
            "christo",
            "oracao",
            "mandamento",
            "proverbio",
            "ezequiel",
            "viacrucis",
            "stop-war",
            "healing-sound",
            "earth-rainbow",
            "yo-webapp",
            "os-10",
        ),
    ),
    (
        "Biblioteca",
        (
            "olavo",
            "ikigai",
            "kaizen",
            "apego",
            "compromisso",
            "dominio",
            "ocaminho",
            "mises",
            "seis-licoes",
            "musashi",
            "suntzu",
            "sun-tzu",
            "notebooklm",
            "devbooks",
            "library-of",
            "cura",
            "plantas",
            "ervas",
            "grande-conflito",
            "12regras",
            "por-que-lutamos",
            "arte-de-alcancar",
        ),
    ),
    (
        "Surf, esporte e litoral",
        (
            "surf",
            "floripa",
            "supsocial",
            "supcamp",
        ),
    ),
    (
        "Memória e tributos",
        (
            "senna",
            "kirk",
            "jornada-seja",
            "estudodamente",
        ),
    ),
]


def gh_graphql(query: str, **variables: str) -> dict:
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for key, value in variables.items():
        cmd.extend(["-f", f"{key}={value}"])
    raw = subprocess.check_output(cmd, text=True, encoding="utf-8")
    return json.loads(raw)


def fetch_owned_public() -> list[dict]:
    query = """
    query($cursor: String) {
      user(login: "araguaci") {
        lists(first: 1) {
          nodes {
            name
            items(first: 100, after: $cursor) {
              pageInfo { hasNextPage endCursor }
              nodes {
                __typename
                ... on Repository {
                  name
                  description
                  url
                  isPrivate
                  isFork
                  homepageUrl
                  primaryLanguage { name }
                  owner { login }
                }
              }
            }
          }
        }
      }
    }
    """
    repos: list[dict] = []
    cursor = ""
    list_name = ""
    while True:
        variables = {"cursor": cursor} if cursor else {}
        payload = gh_graphql(query, **variables)
        node = payload["data"]["user"]["lists"]["nodes"][0]
        list_name = node["name"]
        page = node["items"]
        for item in page["nodes"]:
            if item.get("__typename") != "Repository":
                continue
            if item["owner"]["login"] != OWNER or item["isPrivate"] or item["isFork"]:
                continue
            if item["name"] in EXCLUDE:
                continue
            repos.append(item)
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    if list_name != LIST_NAME:
        raise SystemExit(f"A primeira lista não é {LIST_NAME!r}: {list_name!r}")
    repos.sort(key=lambda repo: repo["name"].lower())
    return repos


def normalize_home(url: str | None) -> str:
    if not url:
        return ""
    url = url.strip()
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return f"https://{url}"


def group_of(name: str) -> str:
    lowered = name.lower()
    for title, keys in GROUPS:
        if any(key in lowered for key in keys):
            return title
    return "Ferramentas, web e experimentos"


def line_compact(repo: dict) -> str:
    name = repo["name"]
    url = repo["url"]
    home = normalize_home(repo.get("homepageUrl"))
    if home and home.rstrip("/") != url.rstrip("/"):
        return f"- [{name}]({url}) · [site]({home})"
    return f"- [{name}]({url})"


def render_compact(repos: list[dict]) -> str:
    buckets: dict[str, list[dict]] = {}
    order = [title for title, _ in GROUPS] + ["Ferramentas, web e experimentos"]
    for repo in repos:
        buckets.setdefault(group_of(repo["name"]), []).append(repo)
    parts = [
        f"<!-- gerado por scripts/sync_public_stack.py em {date.today().isoformat()} -->",
        "",
    ]
    for title in order:
        items = buckets.get(title) or []
        if not items:
            continue
        parts.append(f"**{title}**")
        parts.append("")
        parts.extend(line_compact(repo) for repo in items)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def splice_readme(compact: str, readme_path: str = "README.md") -> None:
    from pathlib import Path

    path = Path(readme_path)
    text = path.read_text(encoding="utf-8")
    start = "<!-- stack:start -->"
    end = "<!-- stack:end -->"
    if start not in text or end not in text:
        raise SystemExit("README.md sem os marcadores stack:start / stack:end")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    path.write_text(
        f"{before}{start}\n{compact}{end}{after}",
        encoding="utf-8",
    )


def line_for(repo: dict) -> str:
    name = repo["name"]
    url = repo["url"]
    desc = (repo.get("description") or "").replace("\n", " ").replace("|", "/").strip()
    lang = (repo.get("primaryLanguage") or {}).get("name") or ""
    home = normalize_home(repo.get("homepageUrl"))
    bits = [f"[{name}]({url})"]
    if lang:
        bits.append(lang)
    if home and home.rstrip("/") != url.rstrip("/"):
        bits.append(f"[site]({home})")
    meta = " · ".join(bits)
    if desc:
        return f"- {meta} — {desc}"
    return f"- {meta}"


def render(repos: list[dict]) -> str:
    buckets: dict[str, list[dict]] = {}
    order = [title for title, _ in GROUPS] + ["Ferramentas, web e experimentos"]
    for repo in repos:
        buckets.setdefault(group_of(repo["name"]), []).append(repo)
    parts = [
        f"<!-- gerado por scripts/sync_public_stack.py em {date.today().isoformat()} -->",
        f"{len(repos)} repositórios públicos originais da lista [My stack](https://github.com/stars/araguaci/lists/my-stack). Privados e forks não entram.",
        "",
    ]
    for title in order:
        items = buckets.get(title) or []
        if not items:
            continue
        parts.append(f"### {title}")
        parts.append("")
        parts.extend(line_for(repo) for repo in items)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    from pathlib import Path

    repos = fetch_owned_public()
    docs = Path("docs")
    docs.mkdir(exist_ok=True)
    full_path = docs / "projetos.md"
    full_path.write_text(
        "# Projetos públicos\n\n"
        "Catálogo gerado a partir da lista [My stack](https://github.com/stars/araguaci/lists/my-stack). "
        "Entram só repositórios públicos de @araguaci que não são fork.\n\n"
        + render(repos),
        encoding="utf-8",
    )
    splice_readme(render_compact(repos))
    print(f"{len(repos)} repos -> {full_path} e README.md", file=sys.stderr)


if __name__ == "__main__":
    main()
