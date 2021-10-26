#!/usr/bin/env python
# coding: utf-8

# # L'ensemble $\mathbb{N}$
# 
# ## Les axiomes de Peano
# 
# L'idée de la construction de $\mathbb{N}$ est assez simple, nous partons de 0, et nous définissons une fonction $S$ injective, appelé successeur.
# 
# L'ensemble $\mathbb{N}$ est alors défini par ce que l'on appelle les axiomes de Peano.
# 
# - L'ensemble possède un élément particulier que l’on note 0.
# - Chaque élément $n$ possède un successeur que l’on note $S(n)$.
# - 0 n'est le successeur d'aucun élément.
# - L'application $S:\mathbb{N} \to \mathbb{N}$ est injective, c'est-à-dire que si deux éléments ont le même successeur, ils sont égaux.
# - Toute partie $\mathbb{N}$ contenant 0 et stable par $S$ est égale à $\mathbb{N}$ tout entier.
# 
# Le premier axiome postule que $\mathbb{N}$ n'est pas vide, le deuxième qu'il est infini et le troisième qu'il a un plus petit élément.  
# Le dernier axiome pose le principe de récurrence dans $\mathbb{N}$ $(0 \in \mathbb{N}, n \in \mathbb{N} \implies S(n) \in \mathbb{N})$.  
# On note $\mathbb{N^{*}}$, l'ensemble $\mathbb{N}$ privé de 0, $\mathbb{N^{*}} = \mathbb{N} \backslash 0$
# 
# ```{prf:proposition} Raisonnement par récurrence
# Soit $P$ une proposition, $k$ un entier naturel tel que  
# **initialisation :** $P(k)$ est vraie  
# **hérédité :** $\forall n \in \mathbb{N} \mid n \geq k, P(n) \implies P(S(n))$  
# Alors la propriété $P$ est vraie pour tout $n \geq k$.
# ```
# 
# ```{prf:definition} Addition, multiplication et puissance
# On définit par récurrence l'addition, noté +, la multiplication, noté $\cdot$ ou $\times$ et la puissance tels que  
# $\forall m, n \in \mathbb{N}$,  
# **addition :** 
# $\begin{align*}
# m + 0 &= m\\
# m + S(n) &= S(m + n)
# \end{align*}$  
# On note $S(0) = 1$ et $\forall n \in \mathbb{N}, \: S(n) = n + 1$  
# **multiplication :**
# $\begin{align*}
# m \cdot 0 &= 0\\
# m \cdot S(n) &= m \cdot n + m
# \end{align*}$  
# **puissance :**
# $\begin{align*}
# m^{0} &= 1\\
# m^{S(n)} &= m^{n} \cdot m
# \end{align*}$
# ```
# 
# ```{prf:property} Propriétés de l'addition et de la multiplication
# $\forall m, n, p \in \mathbb{N}$  
# **commutativité :**
# $\begin{align*}
# m + n &= n + m\\
# m \cdot n &= n \cdot m
# \end{align*}$  
# **associativité :**
# $\begin{align*}
# (m + n) + p &= m + (n + p)\\
# (m \cdot n) \cdot p &= m \cdot (n \cdot p)
# \end{align*}$  
# **distributivité :**
# $m \cdot (n + p) = m \cdot n + m \cdot p$  
# La multiplication $\cdot$ est distributive par rapport à l'addition +  
# 0 est **élément neutre** pour l'addition, $m + 0 = 0 + m = m$  
# 1 est **élément neutre** pour la multiplication, $m \cdot 1 = 1 \cdot m = m$  
# 0 est **élément absorbant** pour la multiplication, $m \cdot 0 = 0 \cdot m = 0$  
# Muni de ces deux **lois de composition interne**, + et $\cdot$, $(\mathbb{N}, +)$ est un **monoïde** commutatif, $(\mathbb{N}, \cdot)$ est un **monoïde** commutatif et $(\mathbb{N}, +, \cdot)$ est un **demi-anneau**.
# ```

# 

# 
