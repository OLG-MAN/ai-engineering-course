# G<N>: <milestone title>

<!-- Copy to gcp/g<N>-<slug>/README.md. Plan and scope: gcp/README.md. -->

| Field | Value |
| --- | --- |
| Upgrades lessons | p11-06, p11-10, … |
| Dates | YYYY-MM-DD → YYYY-MM-DD |
| Time | planned h / actual h |
| Cost | $ total (link to billing report or screenshot) |
| Region / project | <region> / <project id placeholder, not the real one if the repo is public> |

## Architecture

Diagram or short component list: what runs where, how it authenticates, where the data lives.

## Run it

```bash
cd gcp/g<N>-<slug>/terraform && terraform init && terraform apply
# …
terraform destroy
```

## Results

The table the milestone's "done when" asks for.

## Local vs GCP

What the managed version gave me, what it cost (money, latency, lock-in, ops), and when I'd pick each.

## Gotchas

- Quota / availability / IAM surprises, and the lookup command that would have caught them earlier.
