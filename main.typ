#set document(
  title: "TwitchCon Rotterdam 2025 Attendees",
  author: "HappiePlant",
)

#set text(hyphenate: true, font: "Inter", lang: "en")
#set page(margin: 2em)
#set par(spacing: 0em)
#set align(center)

#let data = json("attendees.json")

= TwitchCon Rotterdam 2025 Attendees

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
