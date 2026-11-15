"""Clients for the three LLM providers the pipeline can call.

Keys are read from the environment: ``OPENAI_API_KEY``, ``GOOGLE_API_KEY`` and
``TOGETHER_API_KEY``. Nothing here is imported at package import time by the stages; each
stage imports the client it needs when it runs, so the package installs and the
deterministic stages run without any provider SDK configured.
"""
from __future__ import annotations

import os

PROVIDERS = ("openai", "google", "together")


class MissingAPIKey(RuntimeError):
    """The environment variable holding a provider's API key is not set."""


def require_key(var: str) -> str:
    key = os.getenv(var)
    if not key:
        raise MissingAPIKey(f"Set {var} in the environment before calling this provider.")
    return key


def init_openai_client():
    """OpenAI client (chat completions, Responses API, Batch API)."""
    from openai import OpenAI

    return OpenAI(api_key=require_key("OPENAI_API_KEY"))


def init_together_client():
    """Together client, through its OpenAI-compatible endpoint."""
    from openai import OpenAI

    return OpenAI(api_key=require_key("TOGETHER_API_KEY"), base_url="https://api.together.xyz/v1")


def init_together_sdk_client(timeout: float | None = None):
    """Together's own SDK client, needed for its Batch API (file upload, batch jobs)."""
    try:
        from together import Together
    except ImportError as e:
        raise ImportError("The Together Batch API needs the 'together' package (pip install together).") from e
    kwargs = {"api_key": require_key("TOGETHER_API_KEY")}
    if timeout is not None:
        kwargs["timeout"] = timeout
    return Together(**kwargs)


def init_google_client():
    """Google Gen AI client (generate_content and the batch API)."""
    from google import genai

    return genai.Client(api_key=require_key("GOOGLE_API_KEY"))


def init_google_openai_compatible_client():
    """Gemini through Google's OpenAI-compatible endpoint (chat completions)."""
    from openai import OpenAI

    return OpenAI(api_key=require_key("GOOGLE_API_KEY"),
                  base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


def init_client(provider: str, openai_compatible: bool = False):
    """Client for ``provider`` ("openai", "google" or "together").

    With ``openai_compatible=True`` the Google provider is reached through its
    OpenAI-compatible chat-completions endpoint instead of the Gen AI SDK.
    """
    if provider == "openai":
        return init_openai_client()
    if provider == "together":
        return init_together_client()
    if provider == "google":
        return init_google_openai_compatible_client() if openai_compatible else init_google_client()
    raise ValueError(f"Unknown provider {provider!r}; expected one of {', '.join(PROVIDERS)}")
