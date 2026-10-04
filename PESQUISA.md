# Pesquisa — Controle de versões com Git/GitHub

## 1. O que são branches e como trocar de branches?
Uma branch é uma linha independente de desenvolvimento dentro do Git. Ela permite testar ou desenvolver uma mudança sem alterar imediatamente outra linha do projeto. Para trocar de branch, use `git switch nome-da-branch` ou `git checkout nome-da-branch` em versões antigas do Git.

## 2. Como fazer share/push?
O `git push` envia commits locais para um repositório remoto, como o GitHub. Um fluxo comum é `git add`, `git commit` e depois `git push origin main`. O commit registra a versão local; o push publica essa versão no remoto.

## 3. Como reescrever commit?
Para corrigir o último commit ainda não publicado, pode-se usar `git commit --amend`. Para reescrever commits mais antigos, usa-se rebase interativo. Em histórico já compartilhado, reescrever exige cuidado porque pode alterar os hashes conhecidos por outras pessoas.

## 4. Diferenças entre revert e merge
`git revert` cria um novo commit que desfaz as alterações de um commit anterior, preservando o histórico. `git merge` integra os commits de uma branch em outra e pode gerar um commit de merge quando necessário.

## 5. O que é stage (staging area)?
É a área de preparação entre o diretório de trabalho e o commit. `git add` coloca alterações no stage, permitindo escolher exatamente o que será incluído na próxima versão.

## 6. Para que serve squash de commit?
Squash combina vários commits em um só. É útil para limpar um histórico antes de publicar ou integrar uma funcionalidade, agrupando commits pequenos em uma alteração mais significativa.

## 7. Para que serve reflog?
`git reflog` registra movimentos dos ponteiros locais do Git, como mudanças de branch, reset e commits. Ele é muito útil para localizar estados anteriores que não aparecem mais na história normal.

## 8. Diferenças entre reset e clean
`git reset` altera o estado do histórico/índice e pode mover o `HEAD`, dependendo da opção usada. `git clean` remove arquivos não rastreados do diretório de trabalho. São operações diferentes e devem ser usadas com atenção.
