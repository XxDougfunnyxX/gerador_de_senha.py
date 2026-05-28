"""gerador_de_senha.py

Gerador de senhas 100% via terminal (Python).

Aprendizado (importante):
- Senhas devem usar `secrets` (aleatoriedade criptográfica), não `random`.
- A função precisa receber `tamanho` como INTEIRO.
- As opções (minúsculas/maiúsculas/números/símbolos) precisam realmente afetar os caracteres permitidos.

Rodar:
    python Projetos/gerador_de_senha.py
"""

from __future__ import annotations

import secrets
import string


def ler_bool(mensagem: str) -> bool:
    """Lê (s/n) e converte para bool."""
    resp = input(mensagem).strip().lower()
    if resp in {"s", "sim", "y", "yes"}:
        return True
    if resp in {"n", "nao", "não", "no", "false", "f"}:
        return False
    raise ValueError("Digite 's' ou 'n'.")


def ler_tamanho() -> int:
    """Permite 8, 12 ou 16 (como no seu exemplo), mas com validação clara."""
    tamanho = int(input("Digite o tamanho da senha (8, 12 ou 16): ").strip())
    if tamanho not in {8, 12, 16}:
        raise ValueError("Tamanho inválido. Use 8, 12 ou 16.")
    return tamanho


def gerar_senha(
    *,
    tamanho: int,
    usar_minusculas: bool,
    usar_maiusculas: bool,
    usar_numeros: bool,
    usar_simbolos: bool,
) -> str:
    """Gera uma senha usando `secrets.choice`.

    A ideia é:
    1) montar um conjunto `caracteres` com base nas flags
    2) validar se o conjunto não ficou vazio
    3) escolher `tamanho` caracteres desse conjunto
    """

    if tamanho < 1:
        raise ValueError("tamanho precisa ser >= 1")

    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation  # inclui vários símbolos comuns

    caracteres = ""
    if usar_minusculas:
        caracteres += minusculas
    if usar_maiusculas:
        caracteres += maiusculas
    if usar_numeros:
        caracteres += numeros
    if usar_simbolos:
        caracteres += simbolos

    if not caracteres:
        raise ValueError(
            "Selecione pelo menos um tipo: minúsculas, maiúsculas, números ou símbolos."
        )

    # escolha criptograficamente segura
    return "".join(secrets.choice(caracteres) for _ in range(tamanho))


def main() -> None:
    print("=== Gerador de Senhas (Python) ===")

    tamanho = ler_tamanho()

    usar_maiusculas = ler_bool("Incluir letras maiúsculas? (s/n): ")
    usar_minusculas = ler_bool("Incluir letras minúsculas? (s/n): ")
    usar_numeros = ler_bool("Incluir números? (s/n): ")
    usar_simbolos = ler_bool("Incluir símbolos? (s/n): ")

    try:
        senha = gerar_senha(
            tamanho=tamanho,
            usar_minusculas=usar_minusculas,
            usar_maiusculas=usar_maiusculas,
            usar_numeros=usar_numeros,
            usar_simbolos=usar_simbolos,
        )
        print(f"Senha gerada: {senha}")
    except ValueError as exc:
        print(f"Erro: {exc}")


if __name__ == "__main__":
    main()







