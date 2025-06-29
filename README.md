# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

**Data:** 10/06/2025  
**Empresa:** Abstergo Industries  
**Responsável:** Daniel Paiva

## Introdução

Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por Daniel Paiva. <br>
O objetivo do projeto foi elencar 3 serviços AWS com foco na redução de custos operacionais e de infraestrutura, promovendo escalabilidade e eficiência no uso de recursos computacionais.

## Descrição do Projeto

O projeto de implementação foi dividido em 3 etapas. <br>Cada etapa aborda um serviço da AWS adotado para atender a um problema específico com alto impacto no custo da infraestrutura da empresa.

---

### Etapa 1:  
**Amazon EC2 Auto Scaling**  
**Foco:** Otimização do uso de instâncias computacionais  
**Descrição de caso de uso:**  
A empresa mantinha instâncias EC2 em funcionamento contínuo, mesmo em horários de baixa demanda. <br>O uso do EC2 Auto Scaling permitiu a configuração de políticas automáticas para escalar horizontalmente com base em métricas como uso de CPU e tráfego de rede. <br>Isso reduziu significativamente os custos com instâncias ociosas.

---

### Etapa 2:  
**Amazon S3 + S3 Intelligent-Tiering**  
**Foco:** Armazenamento de dados com otimização automática de custo  
**Descrição de caso de uso:**  
Arquivos armazenados em S3 estavam em classes de armazenamento padrão, independentemente da frequência de acesso. <br>A migração para o S3 Intelligent-Tiering permitiu a movimentação automática dos dados entre classes de acesso frequente e infrequente. <br>Como resultado, houve uma economia de até 40% nos custos mensais com armazenamento.

---

### Etapa 3:  
**AWS Lambda**  
**Foco:** Eliminação de servidores para execução de tarefas esporádicas  
**Descrição de caso de uso:**  
Alguns scripts e processos automatizados rodavam em servidores EC2 dedicados, com baixa frequência de execução. <br>A migração para funções Lambda eliminou a necessidade de manter servidores ligados para tarefas que poderiam ser executadas sob demanda, pagando apenas pelo tempo de execução. <br>Isso proporcionou economia direta em recursos computacionais e manutenção.

---

## Conclusão

A adoção de serviços escaláveis, inteligentes e com cobrança sob demanda da AWS permitiu à Abstergo Industries reduzir custos operacionais, otimizar sua infraestrutura e aumentar a eficiência no uso de recursos. <br> O uso combinado do EC2 Auto Scaling, S3 Intelligent-Tiering e AWS Lambda gerou impacto financeiro positivo já no primeiro mês de operação, servindo como base para futuras iniciativas de modernização e economia em nuvem.

