#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar e desinstalar o `Windows Service for Linux (WSL)` no `Windows`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar e desinstalar o `Windows Service for Linux (WSL)` no `Windows`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using e uninstall the `Windows Service for Linux (WSL)` on `Windows`._

# ## Descrição [2]
# 
# ### `Windows Service for Linux (WSL)`
# 
# O `Windows Subsystem for Linux (WSL)` é uma funcionalidade do `Windows` que permite executar distribuições Linux diretamente no `Windows`, fornecendo uma camada de compatibilidade entre os sistemas operacionais. Com o WSL, os usuários podem executar aplicativos Linux nativos no `Windows` sem a necessidade de virtualização ou dual-boot. Isso permite aos desenvolvedores usar ferramentas e ambientes de desenvolvimento Linux dentro do ambiente familiar do `Windows`, facilitando a transição entre plataformas e aumentando a flexibilidade de desenvolvimento.
# 

# ## 1. Como configurar/instalar/usar o `Windows Service for Linux (WSL)` no `Windows` [1][3]
# 
# Para configurar/instalar/usar o `Windows Service for Linux (WSL)` no `Windows`, você pode seguir estes passos:

# Para instalar o `Linux Ubuntu 22.04 LTS` e o `Kali Linux` via `Windows Subsystem for Linux (WSL) no Windows (WSL)`, siga os passos abaixo. Este guia pressupõe que você esteja utilizando uma versão recente do `Windows 10` ou `Windows 11`.
# 
# 1. **Habilitar o `WSL`:** Abra o `PowerShell` como Administrador e execute o seguinte comando para habilitar o `WSL`: `wsl --install`
# 
#     Esse comando instalará o `WSL` e o necessário para executá-lo. Se o `WSL` já estiver instalado, o comando não fará alterações.
# 
#     1.1 Será solicitado o nome do novo usuário UNIX: `Enter new UNIX username`
# 
#     1.2 Será solicitada a nova senha: `New password`
# 
#     1.3 Será soliciyada a nova senha novamente:  `Retype new password`
# 
# 2. Reinicie seu computador se for solicitado.
# 
# 3. Atualizar para o `WSL 2` (Opcional, mas Recomendado): O WSL 2 oferece um desempenho significativamente melhor e mais recursos em comparação ao WSL 1.
# 
# 4. **Verifique se sua versão do Windows suporta o WSL 2 executando o seguinte comando no PowerShell:**
# 
#     Se o comando acima falhar, siga as instruções fornecidas no terminal para habilitar o `WSL 2`. Pode ser necessário atualizar seu Windows.
# 
#     4.1 Será necessário executar o comando a seguir, pois depois de instalado o `WSL` entra automaticamente no `Linux Ubuntu`:  `exit`
# 
#     4.2 Executar o comando a seguir: `wsl --set-default-version 2`
# 
# 5. Para consultar as distribuições do `Linux` disponíveis para download pelo `PowerShell` para o `Windows Subsystem for Linux (WSL)`, você pode usar o seguinte comando: `wsl --list --online`
# 
# 6. **Instalar o `Ubuntu 22.04 LTS`:** Abra o `Microsoft Store` buscando por ele no menu Iniciar.
# 
# 7. Busque por `"Ubuntu 22.04 LTS"` na `Microsoft Store` e selecione o aplicativo correspondente.
# 
# 8. Clique em `"Instalar"` para começar a instalação. Após a instalação, você pode iniciar o `Ubuntu 22.04 LTS` através do menu Iniciar, ou digite no `Powershell`: `wsl --install ubuntu-22.04`
# 
# 9. **Instalar o `Kali Linux`:** Na `Microsoft Store`, busque por `"Kali Linux"`, ou digite no `PowerShell`: `wsl --install kali-linux`
# 
# 10. Selecione o aplicativo `Kali Linux` e clique em `"Instalar"`.
# 
#     Após a instalação de ambas as distribuições, você pode iniciá-las através do menu Iniciar, procurando por seus nomes.
# 
# 11. **Configuração Inicial:** Na primeira execução de cada distribuição `Linux`, você será solicitado a criar um usuário e senha. Essas credenciais serão usadas para acessar sua distribuição `Linux`.
# 
# **Notas Adicionais**
# 
# - Alternar entre versões do `WSL`: Se precisar alternar uma distribuição específica para usar o `WSL 1` ou `WSL 2`, você pode usar o comando: `wsl --set-version <DistroName> <VersionNumber>`
# 
#     Por exemplo, para definir o `Ubuntu 22.04 LTS` para usar o `WSL 2`, você usaria: `wsl --set-version Ubuntu-22.04 2`
# 
#     Ou para definir o `Kali LInux` para usar o `WSL 2`, você usaria:  `wsl --set-version` 
# 
# - **Atualizações e Gerenciamento:** Você pode gerenciar e atualizar suas distribuições `Linux` através do próprio `Linux`, usando comandos como `sudo apt update` e `sudo apt upgrade` no Ubuntu, ou equivalentes no `Kali Linux`
# .
# Seguindo estes passos, você poderá usar tanto o Ubuntu 22.04 LTS quanto o Kali Linux no Windows através do WSL.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `Windows Service for Linux (WSL)` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     wsl --list --online
#     wsl --install ubuntu-22.04
#     wsl --install kali-linux
#     ```
# 

# ## 2. Ativar uma distribuição pelo `WSL`
# 
# Para `"ativar"` uma distribuição `Linux` no `Windows Subsystem for Linux (WSL)` após a ter instalado, você basicamente inicia a distribuição para usar seus recursos. Se por `"ativar"` você se refere a iniciar a distribuição Linux que você instalou via WSL, isso é feito de forma bastante simples. Aqui estão os passos:
# 
# ### 2.1 Para Iniciar uma Distribuição `Linux` no `WSL`
# 
# 1 **Através do Menu Iniciar:** Você pode simplesmente abrir o menu Iniciar e procurar pelo nome da distribuição `Linux` que você instalou (por exemplo, `"Ubuntu 22.04 LTS"` ou `"Kali Linux"`). Clicar no nome da distribuição abrirá um terminal dessa distribuição.
# Através do `PowerShell` ou Prompt de Comando:
# 
# 2 **Abra o PowerShell ou o Prompt de Comando:** Para iniciar sua distribuição `Linux`, digite o nome da distribuição diretamente no terminal. Por exemplo, se você instalou o `Ubuntu`, pode simplesmente digitar `ubuntu` e pressionar `Enter`. Para o `Kali Linux`, você digitaria `kali` e assim por diante.
# 
# **Nota:** O nome exato do comando para iniciar a distribuição pode variar com base no nome da distribuição que você instalou. Normalmente, é o nome da distribuição sem espaços ou versões. Você pode verificar a documentação específica da sua distribuição para detalhes exatos.
# 
# 3. **Através do `WSL` Command:** Se você quiser iniciar sua distribuição através do comando `wsl`, você pode fazer isso abrindo o `PowerShell` ou o Prompt de Comando e digitando: `wsl -d <NomeDaDistribuição>`
# 
#     Substitua `<NomeDaDistribuição>` pelo nome exato da distribuição que você deseja iniciar, como aparece ao executar `wsl --list`.
# 
#     Uma vez que a distribuição é iniciada, você será colocado no terminal da distribuição, onde você pode começar a executar comandos `Linux` como faria em um ambiente `Linux` padrão.
# 

# ## 3. Para definir uma distribuição como padrão (Opcional)
# 
# 1. Se você trabalha principalmente com uma distribuição `Linux` específica e quer torná-la sua padrão no `WSL`, você pode definir isso com o comando: `wsl --set-default <NomeDaDistribuição>`
# 
# Isso fará com que a distribuição especificada se torne a padrão quando você iniciar o `WSL` sem especificar uma distribuição.
# 

# ## 4. Acessar os diretórios
# 
# ### 4.1 Acessar o disco `C:` do `Windows`
# 
# Para acessar o disco `C:` do `Windows` dentro do `Ubuntu` no `Windows Subsystem for Linux (WSL)`, você pode seguir os passos abaixo. O `WSL` monta automaticamente os discos rígidos do `Windows` sob o diretório `/mnt/`, com cada letra de unidade correspondente tornando-se uma subpasta.
# 
# ### 4.1 Passos para acessar a pasta `C:` do `Windows` no `Ubuntu WSL`
# 
# 1. Abra o `Terminal Emulator` no `Ubuntu` através do `WSL`.
# 
# 2. **Navegue até o diretório de montagem do `Windows`. O disco `C:` do `Windows` geralmente é montado em `/mnt/c/` no `WSL`. Você pode acessar este diretório usando o comando cd no terminal: `cd /mnt/c`
# 
# 3. **Liste o Conteúdo da Pasta. Uma vez no diretório `/mnt/c/`, você pode usar o comando `ls -al` para ver o conteúdo da unidade `C:` do `Windows`**: `ls -al`
# 
#     Isso mostrará os diretórios e arquivos presentes na raiz do seu disco `C:` acessível pelo `WSL`.
# 
# 4. Acessar Arquivos ou Diretórios Específicos. Se você souber o caminho específico de um arquivo ou diretório que deseja acessar, você pode navegar diretamente até ele usando o comando `cd`. Por exemplo, para acessar a pasta `"Usuários"` em `C:`, você usaria: `cd /mnt/c/Users`
# 
# ## 4.2 Dicas Adicionais
# 
# - **Permissões**: Tenha cuidado ao modificar arquivos do sistema `Windows` a partir do `WSL`, pois alterações inapropriadas podem corromper os arquivos.
# 
# - **Uso de Editores e Comandos `Linux`**: Você pode usar editores de texto do `Linux` como `nano` ou `vim` para editar arquivos no disco `C:`, ou executar qualquer comando `Linux` nesses arquivos.
# 
#     Acessar a unidade `C:` desta forma permite que você manipule arquivos entre os sistemas operacionais `Linux` e `Windows` com facilidade, aproveitando o melhor de ambos os ambientes.

# ### 4.2 Acessar o disco `/` do `Linux Ubuntu`
# 
# o Windows Subsystem for Linux (WSL), o diretório raiz do `Linux Ubuntu` (ou de qualquer outra distribuição Linux que você tenha instalado através do WSL) não está localizado em um caminho tradicional acessível através do Explorador de Arquivos do `Windows` de forma simples. Isso ocorre porque o sistema de arquivos do `Linux` é montado dentro de um ambiente virtual gerenciado pelo WSL. No entanto, você ainda pode acessar esses arquivos diretamente do Windows 10 ou Windows 11 seguindo os passos abaixo:
# 
# 1. **Acessando o Diretório do `Linux Ubuntu` no `Windows`**: Acesso Rápido Através do Explorador de Arquivos (Windows 10 e 11): Abra o Explorador de Arquivos. Digite na barra de endereços: `\\wsl$`
# 
#     Isso mostrará todas as distribuições do WSL instaladas.
# 
#     Você encontrará sua distribuição do `Ubuntu` listada, algo como `\\wsl$\Ubuntu` ou `\\wsl$\Ubuntu-22.04`, dependendo da versão que você instalou.
# 
# Ao clicar nesta pasta, você estará acessando o diretório raiz do `Ubuntu`.

# ## 5. Desinstalar uma distribuição no `WSL`
# 
# Para desinstalar uma distribuição Linux no Windows Subsystem for Linux (WSL), você pode seguir os passos abaixo. Este processo irá remover a distribuição selecionada, juntamente com todos os dados, software e configurações nela contidos.
# 
# 1. **Abra o `PowerShell` como Administrador:** Liste as distribuições instaladas para encontrar o nome exato da distribuição que você deseja desinstalar. Você pode fazer isso com o comando: `wsl --list`
# 
# 2. Desinstale a distribuição desejada utilizando o comando `wsl --unregister`. Por exemplo, se você quiser desinstalar o `Ubuntu 22.04`, substitua <NomeDaDistribuição> pelo nome exato da distribuição conforme aparece na lista: `wsl --unregister <NomeDaDistribuição>`
# 
#     2.1 Por exemplo, se o nome da sua distribuição for `"Ubuntu-22.04"`, o comando seria: `wsl --unregister Ubuntu-22.04`
# 
#     Este comando irá desinstalar a distribuição selecionada, removendo-a do seu sistema. Se mais tarde você decidir reinstalá-la, precisará seguir o processo de instalação novamente, o que criará uma nova instância da distribuição sem os dados anteriores.
# 
# Lembre-se de que este processo é irreversível, e todos os dados na distribuição serão perdidos. Certifique-se de fazer backup de quaisquer dados importantes antes de prosseguir com a desinstalação.

# ## Referências
# 
# [1] OPENAI. ***Instalar ubuntu e kali via wsl.*** Disponível em: <https://chat.openai.com/c/202844dd-74a6-44c2-8542-9948a356060c> (texto adaptado). Acessado em: 29/03/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 29/03/2024 17:10.
# 
