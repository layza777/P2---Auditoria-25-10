# Auditoria I — Cosan S.A. — Exercício 2025

**Preparadora:** Láyza Cristina Fernandes de Albuquerque  
**Matrícula:** 221002998  
**Data de análise:** 24/10/2026

**Natureza:** trabalho acadêmico baseado em documentos públicos e simulações didáticas. Não é auditoria profissional e não expressa opinião independente.

## Estrutura do repositório
- `01_Dossie/Dossie_Auditoria_Cosan_2025.pdf` — dossiê acadêmico com papéis de trabalho, conclusão e limitações.
- `02_Planilhas/Planilha_Auditoria_Cosan_2025.xlsx` — materialidade, saldos, matriz de riscos, amostragem, fontes e programas de auditoria.
- `02_Planilhas/matriz_de_riscos.csv` — matriz de riscos em formato CSV.
- `02_Planilhas/matriz_cobertura_normas.csv` — matriz de cobertura das normas e papéis de trabalho.
- `03_Base_Sintetica/amostra_sintetica_400.csv` — amostra ilustrativa de 400 linhas.
- `03_Base_Sintetica/resultados_testes_sinteticos.csv` — resultados de testes de integridade e exceções didáticas.
- `03_Base_Sintetica/base_caixa_sintetica_500000.csv.gz` — base com 500.000 registros sintéticos.
- `03_Base_Sintetica/dicionario_de_dados.csv` — definição das variáveis da base.
- `03_Base_Sintetica/resumo_conciliacao.json` — resumo da conciliação aritmética.
- `04_Codigos/gerar_e_testar_base.py` — código de geração e análise.
- `05_Fontes/registro_de_fontes.csv` — registro de fontes e referências.

## Fontes principais
1. Demonstrações financeiras individuais e consolidadas de 2025, incluindo relatório do auditor independente: https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?CodigoTipoInstituicao=1&NumeroSequencialDocumento=155203
2. Relações com Investidores da Cosan: https://ri.cosan.com.br/
3. Release de resultados 4T25 e 2025.

A data de análise indicada no trabalho é 24/10/2026.

## Base sintética e limitações
A base contém registros integralmente sintéticos, com instituições e instrumentos fictícios. Seu total foi calibrado aritmeticamente para corresponder ao saldo público de caixa e equivalentes de caixa consolidados de R$ 27.243.683 mil em 31/12/2025. Essa correspondência não comprova a existência dos instrumentos nem constitui evidência real da Cosan. As exceções foram inseridas para fins didáticos e não representam erros constatados na companhia. Não projetar resultados da base para a entidade real.

## Como reproduzir
Requer Python 3, `numpy` e `pandas`.
```bash
python 04_Codigos/gerar_e_testar_base.py --output 03_Base_Sintetica/base_caixa_sintetica_500000.csv.gz
python 04_Codigos/gerar_e_testar_base.py --input 03_Base_Sintetica/base_caixa_sintetica_500000.csv.gz
```

## Escopo e limitações
Os procedimentos baseados em fontes públicas, os planejados por falta de acesso e os simulados devem permanecer claramente distinguidos. Não foram realizadas confirmações externas reais, inspeções físicas, entrevistas ou acessos a sistemas internos. O documento não expressa opinião profissional independente.
