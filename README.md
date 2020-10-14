# Infrastructure Tracking Schema
This repository contains a concept for a infrastructure tracking ruleset schema written for
[Yamale](https://pypi.org/project/yamale).

## Rule based queries
While this repository does **not** implement software for querying various services, the goal is to have a common rule
schema that allows querying a variety of services and chaining those queries together. An example rule could look like
this:

```yaml
title: Example Rule
uuid: 11d0a892-b2eb-4df5-8b04-3a1272da6eed
author: Nils Kuhnert
status: experimental
created: 2020-10-09
classification:
  - type: tlp
    value: white
condition:
  - AND:
    - type: "shodan"
      query: "HTTP/1.1 200 X-Super-Suspicious-Header: Honk!"
    - type: "passivedns"
      query: "regex:^\\w-\\w\\.site$"
```

Various services and their queries can be implemented in your own tooling in your own way. The key idea is to combine
multiple data sources right from the start and to have a (mostly) readable ruleset.
[The complex example rule](examples/rule.yml) shows all currently possible rule keys implemented in the
[schema](schema.yml). 