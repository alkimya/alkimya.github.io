#!/usr/bin/env python
# coding: utf-8

# # Logique et langage mathématique
# 
# En mathématiques, nous nous attachons à démontrer la véracité d'une proposition, et la logique mathématique est le fondement des mathématiques.  
# Il n'y a pas dans les mathématiques d'ambiguïté, comme dans la langue et le mathématicien a horreur des contradictions, mais il adore les paradoxes.
# 
# ```{prf:definition} Proposition - Principe du tiers exclu
# :label: tiers-exclu
# Une **proposition** logique est soit **vraie**, soit **fausse** mais pas les deux en même temps.
# ```
# 
# ## Les connecteurs logiques
# 
# ```{prf:definition} Négation $\lnot$ 'non'
# :label: negation
# Soit $P$ une proposition, alors $\lnot P$ est une proposition.  
# $\lnot P$ se lit **non** $P$.
# ```
# 
# Si $P$ est vraie alors $\lnot P$ est fausse et, si $P$ est fausse alors $\lnot P$ est vraie.
# 
# On forme ce que l'on appelle une table de vérité afin de visualiser et calculer la valeur d'une proposition.
# 
# Table de vérité de $\lnot P$
# 
# $P$ | $\lnot P$
# ----|---------
# 1   | 0
# 0   | 1
# 
# J'utilise des valeurs numériques, 1 pour vrai et 0 pour faux, mais souvent on voit V et F dans les tables de vérité.  
# La négation est le seul connecteur logique unaire, qui ne prend qu'une proposition.
# 
# Nous allons voir maintenant les connecteurs binaires.
# 
# ```{prf:definition} Disjonction $\lor$ 'ou'
# :label: disjonction
# Soit $P$ et $Q$ deux propositions, alors $P \lor Q$ est une proposition.  
# $P \lor Q$ se lit $P$ **ou** $Q$
# ```
# 
# $P \lor Q$ est vraie si l'une des propositions est vraie, ou si les deux sont vraies.  
# $P \lor Q$ est fausse si les deux propositions sont fausses.
# 
# Table de vérité de $P \lor Q$
# 
# $P$ | $Q$ | $P \lor Q$
# ----|-----|-----------
# 1   | 1   | 1
# 1   | 0   | 1
# 0   | 1   | 1
# 0   | 0   | 0
# 
# On peut contruire tous les autres connecteurs logiques à partir de ces deux connecteurs $\lnot$ et $\lor$.
# 
# En mathématiques, on commence avec des notations simples, qui lorsqu'on les combine, se compléxifient, alors on pose de nouvelles notations afin de tout simplifier.  
# On fera cela tout le temps en mathématiques...
# 
# ```{prf:definition} Conjonction $\land$ 'et'
# :label: conjonction
# Soit $P$  et $Q$ deux propositions, la proposition $\lnot (\lnot P \lor \lnot Q)$ [non(non $P$ ou non $Q$)] se note $P \land Q$.  
# $P \land Q$ se lit $P$ **et** $Q$.
# ```
# 
# Comme combinaison de $\lnot$ et de $\lor$, $P \land Q$ est une proposition, qui est vraie seulement si les deux proposition $P$ et $Q$ sont vraies à la fois.
# 
# Table de vérité de $P \land Q$
# 
# $P$ | $Q$ | $\lnot P$ | $\lnot Q$ | $\lnot P \lor \lnot Q$ | $\lnot (\lnot P \lor \lnot Q) \equiv P \land Q$
# ----|-----|----------|----------|----------------------|----------------------------------------------
# 1   | 1   | 0        | 0        | 0                    | 1
# 1   | 0   | 0        | 1        | 1                    | 0
# 0   | 1   | 1        | 0        | 1                    | 0
# 0   | 0   | 1        | 1        | 1                    | 0
# 
# ```{prf:definition} Implication $\implies$
# :label: implication
# Soit $P$ et $Q$ deux propositions, la proposition $\lnot P \lor Q$ se note $P \implies Q$.  
# $P \implies Q$ se lit $P$ **implique** $Q$.
# ```
# 
# $P \implies Q$ est fausse si $P$ est vraie et $Q$ est fausse, elle est vraie autrement.
# 
# Table de vérité de $P \implies Q$
# 
# $P$ | $Q$ | $\lnot P$ | $\lnot P \lor Q \equiv P \implies Q$
# ----|-----|----------|------------------------------------
# 1   | 1   | 0        | 1
# 1   | 0   | 0        | 0
# 0   | 1   | 1        | 1
# 0   | 0   | 1        | 1
# 
# Il est intéressant de remarquer que connaître la véracité de $P$, ne permet pas de déduire celle de $P \implies Q$, en revanche si $Q$ est vraie alors $P \implies Q$ l'est aussi et si $P$ est fausse alors $P \implies Q$ est vraie...  
# Si on a $P \implies Q$ vraie, alors on dit que $P$ est **une condition suffisante** de $Q$, $Q$ est **une condition nécessaire** de $P$.
# 
# ```{prf:definition} Équivalence $\iff$
# :label: equivalence
# Soient $P$ et $Q$ deux propositions, la proposition $(P \implies Q) \land (Q \implies P)$ se note $P \iff Q$.  
# $P \iff Q$ se lit P **est équivalent à** Q.
# ```
# 
# $P \iff Q$ est vraie lorsque les deux propositions $P$ et $Q$ ont les mêmes valeurs logiques.
# 
# Table de vérité de $P \iff Q$
# 
# $P$ | $Q$ | $P \implies Q$ | $Q \implies P$ | $(P \implies Q) \land (Q \implies P) \equiv P \iff Q$
# ----|-----|----------------|----------------|-------------------------------------------------------
# 1   | 1   | 1              | 1              | 1
# 1   | 0   | 0              | 1              | 0
# 0   | 1   | 1              | 0              | 0
# 0   | 0   | 1              | 1              | 1
# 
# Si deux propositions sont équivalentes alors elles ont la même table de vérité.
# 
# ```{prf:definition} Tautologie - Contradiction
# Une **tautologie** est une proposition toujours vraie.  
# Une **contradiction** est une proposition toujours fausse.
# ```
# 
# ```{prf:example}
# $P \lor \lnot P$ est une tautologie  
# $P \land \lnot P$ est une contradiction [(Principe du tiers exclus)](https://fr.wikipedia.org/wiki/Principe_du_tiers_exclu)
# ```
# 
# ### Quelques équivalences à connaître
# 
# ```{prf:proposition}
# Soit $P$, $Q$ et $R$ des propositions
# 
# **Double négation :** $\quad \lnot (\lnot P) \iff P$
# 
# **Idempotence :** $\quad P \lor P \iff P \:$ et $\: P \land P \iff P$
# 
# **Commutativité :** $\quad (P \lor Q) \iff (Q \lor P)\:$ et $\:(P \land Q) \iff (Q \land P)$
# 
# **Associativité :** $\quad ((P \lor Q) \lor R) \iff (P \lor (Q \lor R))\:$ et $\:((P \land Q) \land R) \iff (P \land (Q \land R))$
# 
# **Dualité - [Lois de Morgan](https://fr.wikipedia.org/wiki/Lois_de_De_Morgan):** $\quad \lnot (P \lor Q) \iff (\lnot P) \land (\lnot Q)\:$ et $\: \lnot (P \land Q) \iff (\lnot P) \lor (\lnot Q)$
# 
# **Distributivité :** $\quad (P \lor (Q \land R)) \iff (P \lor Q) \land (P \lor R)\:$ et $\: (P \land (Q \lor R)) \iff (P \land Q) \lor (P \land R)$
# ```
# 
# > On peut, à titre d'exercices comme des sudokus, démontrer ces équivalences avec des tables de vérité.
# 
# ## Ensemble et prédicat
# 
# ```{prf:definition} Ensemble - Élément
# :label: ensemble
# Un **ensemble** $E$ est une collection d'objets, appelés **élements**.  
# Un élement $x$ appartient à $E$ se note $\: x \in E$.  
# Un élement $x$ n'appartient pas à $E$ se note $\: x \notin E$.  
# Il existe un ensemble, l'_**ensemble vide**_, noté $\: \varnothing$, qui ne contient aucun élément.
# ```
# 
# Deux ensembles $E$ et $F$ sont égaux s'ils ont les mêmes élements.
# 
# ```{prf:definition} Prédicat
# Soit $E$ un ensemble.  
# Un **prédicat** $P(x)$ dans $E$ est une proposition dont la valeur logique dépend d'une variable $x$ appartenant à $E$.
# ```
# 
# $P(x)$ est vrai, est souvent noté juste $P(x)$.
# 
# ### Quantificateurs
# 
# Soit $E$ un ensemble, $P(x)$ un prédicat dans $E$
# 
# ```{prf:definition} Le quantificateur universel $\forall$ 'pour tout'
# :label: universel
# La proposition, **pour tout** élément $x$ appartenant à $E$, $P(x)$ est vrai se note $\: \forall x \in E, P(x)$.
# ```
# 
# Dire $\forall x \in E, P(x)$, c'est ne pas faire de supposition sur $x$, on le prend 'au hasard' et la proposition P est vraie, pour n'importe quel $x$.
# 
# ```{prf:definition} Le quantificateur existentiel $\exists$ 'il existe'
# :label: existentiel
# La proposition, **il existe au moins** un élément $x$ appartenant à $E$ tel que $P(x)$ est vrai se note $\: \exists x \in E \mid P(x)$.  
# La proposition, **il existe un et un seul** élément $x$ appartenant à $E$ tel que $P(x)$ est vrai se note $\: \exists ! x \in E \mid P(x)$.
# ```
# 
# La barre verticale (ou oblique parfois) $\mid$ se lit 'tel que', et le point d'exclamation ! se lit 'unique'.
# 
# Dire $\exists x \in E \mid P(x)$, c'est exhiber, trouver un $x$ dans $E$ tel que $P(x)$ soit vrai.  
# Dire $\exists ! x \in E \mid P(x)$, c'est trouver un $x$ dans $E$ tel que $P(x)$ et montrer que si deux éléments $x$ et $x'$ appartenant à $E$ tel que $P(x)$ et $P(x')$ alors $x = x'$.
# 
# On a pour les propositions contenant des quantificateurs, l'équivalent des lois de Morgan.
# 
# ```{prf:proposition} Lois de Morgan
# $\: \lnot (\forall x \in E, P(x)) \iff \exists x \in E \mid \lnot P(x)\:$ et $\: \lnot (\exists x \in E \mid P(x)) \iff \forall x \in E, \lnot P(x)$
# ```
# 
# ## Les raisonnements
# 
# ```{prf:proposition} Modus ponens
# :label: modus-ponens
# Soit $P$ et $Q$ deux propositions, alors on a  $\: (P \land (P \implies Q)) \implies Q$
# ```
# Si $P$ est vraie et $P \implies Q$ est vraie alors $Q$ est vraie.  
# C'est le raisonnement déductif classique, on démontre un résultat en partant des hypothèses.
# 
# ```{prf:proposition} Contraposée
# :label: contraposee
# Soit $P$ et $Q$ deux propositions, alors on a  
# $\: (P \implies Q) \iff (\lnot Q \implies \lnot P)$
# ```
# Si $P$ implique $Q$, on peut, et il suffit de montrer que non $Q$ implique non $P$.
# 
# ```{prf:proposition} Preuve par l'absurde
# :label: absurde
# Soit $P$ et $Q$ deux propositions, alors on a  
# $\:((\lnot P \implies Q) \land \lnot Q) \implies P$
# ```
# Pour montrer que $P$ est vraie, on la suppose fausse et on montre que cela entraîne une proposition fausse, alors que l'on sait que celle-ci est vraie.
# 
# ```{prf:proposition} Syllogisme
# :label: syllogisme
# Soit $P$, $Q$ et $R$ trois propositions, alors on a  
# $((P \implies Q) \land (Q \implies R)) \implies (P \implies R)$
# ```
# 
# ```{prf:proposition} Disjonction des cas
# Soit $P$, $Q$ et $R$ trois propositions, alors on a  
# $((P \implies R) \land (Q \implies R)) \implies ((P \lor Q) \implies R)$
# ```
# 
# Nous verrons le raisonnement par récurrence après avoir construit $\mathbb{N}$.
# 

# 
