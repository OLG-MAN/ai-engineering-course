# Learning lab: stable tools baked in, Python packages from requirements.txt.
# Rebuild after changing requirements.txt: `make rebuild`.
FROM python:3.12-slim-bookworm

ARG KUBECTL_VERSION=v1.36.5
ARG TARGETARCH

RUN apt-get update \
 && apt-get install -y --no-install-recommends git curl ca-certificates make less jq procps bash-completion \
 && rm -rf /var/lib/apt/lists/*

RUN curl -fsSLo /usr/local/bin/kubectl "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/${TARGETARCH}/kubectl" \
 && chmod +x /usr/local/bin/kubectl \
 && kubectl completion bash > /etc/bash_completion.d/kubectl

COPY --from=ghcr.io/astral-sh/uv:0.13.8 /uv /uvx /usr/local/bin/

RUN useradd --create-home --uid 1000 --shell /bin/bash dev
ENV VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:/home/dev/.local/bin:$PATH \
    UV_LINK_MODE=copy
# /cache is a named volume; creating it here makes the volume dev-owned on first use
RUN uv venv "$VIRTUAL_ENV" && mkdir -p /cache && chown -R dev:dev "$VIRTUAL_ENV" /cache \
 && echo 'export VIRTUAL_ENV=/opt/venv PATH="/opt/venv/bin:$HOME/.local/bin:$PATH"' > /etc/profile.d/10-venv.sh

USER dev
COPY --chown=dev:dev requirements.txt /tmp/requirements.txt
RUN uv pip install --no-cache -r /tmp/requirements.txt \
 && uv tool install pre-commit==4.7.0 \
 && echo 'source /etc/bash_completion; alias k=kubectl; complete -o default -F __start_kubectl k' >> /home/dev/.bashrc

COPY --chmod=755 .devcontainer/entrypoint.sh /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["sleep", "infinity"]
