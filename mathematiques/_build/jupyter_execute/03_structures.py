#!/usr/bin/env python
# coding: utf-8

# # Structures algébriques
# 
# ## Loi de composition interne
# 
# ```{prf:definition} Loi de composition interne
# Soit $E$ un ensemble.  
# Une **loi de composition interne**, **lci** en abrégé, dans $E$ est une application $\star$ de $E \times E$ dans $E$, $\star$ est une opération binaire stable par $E$.  
# $\forall x, y \in E, \: x \star y \in E$.  
# ```
# 
# ```{prf:definition} Magma
# Un **magma** est un ensemble , l'ensemble $M$ muni d'une lci $\star$, et se note $(M, \star)$
# ```
# 
# ```{prf:definition} Commutativité - Associativité
# Soit $(M, \star)$ un magma.  
# $(M, \star)$ est **commutatif** si $\forall x, y \in (M, \star), x \star y = y \star x$.  
# $(M, \star)$ est **associatif** si $\forall x, y, z \in (M, \star), (x \star y) \star z = x \star (y \star z)$  
# ```
# 
# ```{prf:definition} Idempotence
# Soit $(M, \star)$ un magma, $x$ un élément de $(M, \star)$.  
# $x$ est **idempotent** si $x \star x = x$
# ```
# 
# ```{prf:definition} Neutre - Unifère
# Soit $(M, \star)$ un magma.  
# Un élement $e$ de $(M, \star)$ est un **élément neutre** si $\forall x \in (M, \star), x \star e = e \star x = x$  
# $(M, \star)$ est **unifère** ou **unitaire**, l'élément $e$ est idempotent et unique.
# ```
# 
# ```{prf:definition} Absorbant
# Soit $(M, \star)$ un magma.  
# Un élément $a$ de $(M, \star)$ est un **élément absorbant** pour $\star$ si $\forall x \in E, x \star a = a \star x = a$.  
# L'élément $a$ est idempotent et unique.
# ```
# 
# ```{prf:definition} Monoïde
# Soit $(M, \star)$ un magma.  
# $(M, \star)$ est un **monoïde** si $(M, \star)$ est unifère et associatif.
# ```
# 
# ## Groupe
# 
# ```{prf:definition} Symétrique
# Soit $(M, \star)$ un monoïde, $x$ un élément de $(M, \star)$.  
# ```
# 
# ```{prf:definition} Groupe
# ```
# 
# ## Anneau
# 
# ```{prf:definition} Anneaux
# ```
# 
# ## Corps
# 
# ```{prf:definition} Corps
# ```

# 
