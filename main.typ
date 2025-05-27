// Config (more in main.py)
#let title = "TwitchCon Rotterdam 2025 Attendees"
#let font = "Inter"
#let author = "HappiePlant"

#set document(
  title: title,
  author: author,
)

#set text(hyphenate: true, font: font, lang: "en")
#set page(margin: 2em)
#set par(spacing: 0em)
#set align(center)

#let data = json("attendees.json")

= #title

#v(1em)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  rows: auto,
  gutter: 1em,

  ..data
    .attendees
    .sorted(key: k => lower(k.name))
    .map(it => link(it.url)[
      #image("img_res/" + it.avatar.split("/").last(), height: 10%)
      #v(0.5em)
      #(
        it
          .name
          .replace("_", "_" + str(sym.zws))
          .replace(regex("([a-z])([A-Z])"), it => it.captures.at(0) + sym.zws + it.captures.at(1))
      )
    ])
)
