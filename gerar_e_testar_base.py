#!/usr/bin/env python3
"""
Base didática sintética de caixa e equivalentes de caixa.
ATENÇÃO: todos os registros são fictícios e NÃO são dados reais da Cosan.
A única informação real utilizada como alvo de conciliação é o saldo publicado:
R$ 27.243.683 mil em 31/12/2025 (demonstrações financeiras, nota 5.2).
"""
import argparse
from datetime import date
import numpy as np
import pandas as pd

SEED = 20261025
N = 500_000
SALDO_PUBLICADO_R = 27_243_683_000.00

def generate(path, n=N, seed=SEED):
    rng = np.random.default_rng(seed)
    weights = rng.lognormal(mean=0.0, sigma=1.0, size=n)
    total_cents = int(round(SALDO_PUBLICADO_R * 100))
    raw = weights / weights.sum() * (total_cents - n)
    cents = np.floor(raw).astype(np.int64) + 1
    remainder = int(total_cents - cents.sum())
    if remainder > 0:
        cents[np.argsort(raw - np.floor(raw))[-remainder:]] += 1
    elif remainder < 0:
        cents[np.argsort(cents)[::-1][:(-remainder)]] -= 1
    amounts = cents / 100.0
    open_ord = rng.integers(date(2024,1,1).toordinal(), date(2025,12,31).toordinal()+1, size=n)
    open_dates = [date.fromordinal(int(x)).isoformat() for x in open_ord]
    maturity_days = rng.integers(-180, 540, size=n)
    maturity_ord = date(2025,12,31).toordinal() + maturity_days
    maturity_dates = [date.fromordinal(int(max(date(2023,1,1).toordinal(), min(date(2027,12,31).toordinal(), x)))).isoformat() for x in maturity_ord]
    banks = rng.choice(["Banco Sintético A","Banco Sintético B","Banco Sintético C","Banco Sintético D","Banco Sintético E"], size=n)
    types = rng.choice(["CDB sintético","Fundo DI sintético","Título público sintético","Depósito a prazo sintético"], size=n)
    interest = np.round(amounts * rng.uniform(0,.04,size=n), 2)
    principal = np.round(amounts - interest, 2)
    matured = np.array([d < "2025-12-31" for d in maturity_dates])
    exception = matured.copy()
    reason = np.where(matured, "Vencimento anterior à data-base: investigar liquidação/cut-off", "")
    candidates = np.where(~matured)[0]
    extra = rng.choice(candidates, size=min(50,len(candidates)), replace=False)
    exception[extra] = True
    reason[extra] = "Confirmação externa simulada ausente: aplicar procedimento alternativo"
    df = pd.DataFrame({
        "id_registro_sintetico": [f"SYN-{i:06d}" for i in range(1,n+1)],
        "empresa_referencial": "Cosan S.A. - referência pública; não é razão auxiliar real",
        "conta_referencial": "Caixa e equivalentes de caixa",
        "instituicao_ficticia": banks,
        "tipo_instrumento_sintetico": types,
        "data_aplicacao": open_dates,
        "data_vencimento_sintetica": maturity_dates,
        "principal_sintetico_R$": principal,
        "juros_acumulados_sinteticos_R$": interest,
        "saldo_final_sintetico_R$": amounts,
        "confirmacao_externa_simulada": np.where(np.isin(np.arange(n), extra), "Ausente - exceção didática", "Não executada; campo sintético"),
        "excecao_didatica": exception.astype(int),
        "motivo_excecao_didatica": reason,
        "origem_dados": "100% sintético; gerado por código; não representa transações reais da Cosan"
    })
    df.to_csv(path, index=False, compression="gzip", float_format="%.2f")
    return df

def analyze(path):
    df = pd.read_csv(path, compression="gzip")
    tests = {
        "quantidade_registros": len(df),
        "ids_unicos": int(df["id_registro_sintetico"].nunique()),
        "ids_duplicados": int(df["id_registro_sintetico"].duplicated().sum()),
        "saldo_total_sintetico_R$": round(float(df["saldo_final_sintetico_R$"].sum()),2),
        "saldo_publicado_referencia_R$": SALDO_PUBLICADO_R,
        "diferenca_conciliacao_R$": round(float(df["saldo_final_sintetico_R$"].sum())-SALDO_PUBLICADO_R,2),
        "registros_com_excecao_didatica": int(df["excecao_didatica"].sum()),
        "saldo_medio_sintetico_R$": round(float(df["saldo_final_sintetico_R$"].mean()),2),
    }
    print(pd.Series(tests).to_string())
    return tests

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--output", default="base_caixa_sintetica_500000.csv.gz")
    p.add_argument("--input", default=None)
    p.add_argument("--rows", type=int, default=N)
    args = p.parse_args()
    if args.input:
        analyze(args.input)
    else:
        generate(args.output, args.rows)
        analyze(args.output)
