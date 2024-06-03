---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3.9.7 64-bit
  name: python3
---

# Structures algébriques

## Loi de composition interne

```{prf:definition} Loi de composition interne
Soit $E$ un ensemble.  
Une **loi de composition interne** $\star$, **lci** en abrégé, dans $E$ est une relation binaire, interne et stable, de $E \times E$ dans $E$  
$\forall x, y \in E, \: x \star y \in E$.  
```

```{prf:definition} Magma
Un **magma** est un ensemble , l'ensemble $M$ muni d'une lci $\star$, et se note $(M, \star)$
```

```{prf:definition} Commutativité - Associativité
Soit $(M, \star)$ un magma.  
$(M, \star)$ est **commutatif** si $\forall x, y \in (M, \star), x \star y = y \star x$.  
$(M, \star)$ est **associatif** si $\forall x, y, z \in (M, \star), (x \star y) \star z = x \star (y \star z)$  
```

```{prf:definition} Idempotence
Soit $(M, \star)$ un magma, $x$ un élément de $(M, \star)$.  
$x$ est **idempotent** si $x \star x = x$
```

```{prf:definition} Neutre - Unitaire
Soit $(M, \star)$ un magma. Un élement $e$ de $(M, \star)$ est 
- un **neutre à gauche** si $\forall x \in (M, \star), e \star x = x$  
- un **neutre à droite** si $\forall x \in (M, \star), x \star e = x$..
- un **neutre** s'il est neutre à gauche et à droite.
$(M, \star)$ est **unitaire** ou **unifère**
```

```{prf:property} Propriété du neutre
Soit $(M, \star)$ un magma, $e$ élément neutre de $(M, \star)$  
$e$ est idempotent et unique
```

```{prf:definition} Absorbant
Soit $(M, \star)$ un magma. Un élément $a$ de $(M, \star)$ est 
- un **absorbant à gauche** si $\forall x \in (M, \star), a \star x = a$.  
- un **absorbant à droite** si $\forall x \in (M, \star), x \star a = a$.  
- un **absorbant** s'il est absorbant à gauche et à droite.
```

```{prf:property} Propriété de l'absorbant
Soit $(M, \star)$ un magma, $a$ élément absorbant de $(M, \star)$  
$a$ est idempotent et unique
```

```{prf:definition} Monoïde
Soit $(M, \star)$ un magma.  
$(M, \star)$ est un **monoïde** si $(M, \star)$ est unitaire et associatif.
```

## Groupe

```{prf:definition} Symétrique
Soit $(M, \star)$ un monoïde, $e$ le neutre de $(M, \star)$.
 Un élément $x$ de $(M, \star)$ est  
- **symétrisable à gauche** si $\exists x^{´} \in (M, \star) | x^{´} \star x = e  
- **symétrisable à droite** si $\exists x^{´} \in (M, \star) | x \star x^{´} = e  
- **symétrisable** s'il est symétrisable à gauche et à droite,  $x^{´}$ est le symétrique de $x$ et est noté $x^{-1}$
```

```{prf:definition} Groupe - Groupe abélien
Soit $(G, \star)$ un monoïde.  
$(G, \star)$ est un **groupe** si tout élément non absorbant est symétrisable.  
$(G, \star)$ est un **groupe abélien ou groupe commutatif** si $(G, \star)$ est commutatif.
```

## Anneau

```{prf:definition} Distributivité
Soit $A$ un ensemble, $\star$ et $\star^{´}$ deux lci dans $A$.  
$A$ muni des deux lci $\star$ et $\star^{´} se note $(A, \star, \star^{´})$  
$\star^{´}$ est **distributive** par rapport à $\star$ si,  
$\forall x, y, z \in (A, \star, \star^{´}), x \star^{´} (y \star z) = (x \star^{´} y) \star (x \star^{´} z)$
```

```{prf:definition} Anneaux
Soit $A$ un ensemble, $\star$ et $\star^{´}$ deux lci dans $A$.
$(A, \star, \star^{´})$ est un anneau si  
- $(A, \star)$ est un groupe abélien  
- $\star^{´}$ est associative, et distributive par rapport à $\star$
```

```{prf:definition} Anneau commutatif - Unitaire
Soit $(A, \star, \star^{´})$ un anneaux, $(A, \star, \star^{´})$ est un anneau  
- **commutatif** si $(A, \star^{´})$ est un magma commutatif  
- **unitaire** si $(A, \star^{´})$ est un monoïde  
```

## Corps

```{prf:definition} Corps
Soit $(K, \star, \star^{´})$ un anneaux,  
$(K, \star, \star^{´})$ un corps si $(K, \star)$ est un groupe.  
```

+++
