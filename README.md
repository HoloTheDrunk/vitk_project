# vitk_project

### Raphaël Duhen, Maël Conan, Nigel Andrews

Dans ce document, nous allons présenter notre implémentation du projet, les difficultés rencontrées, ainsi que les divers résultats.

Nous avons également implémenté le projet sur un VSC Share, ce qui fait que les contributions de tout le monde n'apparaissent pas dans l'historique GIT, mais tout le monde a bel et bien participé au projet.

## Recalage d'image

### Pre-traitements

Avant de commencer le recalage, nous avons effectué plusieurs pre-traitements afin de pouvoir avoir des images plus propres et donc plus facilement recalables.

Nous avons donc effectué les pre-traitements suivants :
- itk.median_image_filter : permet de supprimer les bruits de l'image
- itk.ResampleImageFilter : permet de redimensionner l'image afin d'avoir des images de même taille

### Approche initiale: transformation rigide

Dans un premier temps, nous sommes parti sur une transformation rigide pour notre recalage d'image.
Cependant, nous nous sommes confrontés à un problème : des rotations non désirées intervenaient dans le processus de transformation.

Après plusieurs recherches, un des possibles problèmes était la transformation rigide. Nous nous sommes donc dirigés vers un autre type de transformation.

### Approche finale: transformation par translation

L'approche finalement utilisée est une transformation par translation. En effet, avec ce type de transformation notre probleme de rotation de l'image pendant la transformation.

Egalement, pour atteindre tout cela, nous utilisons une registration avec les étapes suivantes :
- un optimizer : itk.RegularStepGradientDescentOptimizerv4
- des metrics: itk.MeanSquaresImageToImageMetricv4
- et enfin un registration: itk.ImageRegistrationMethodv4

### Illustration

Pour illustrer notre recalage, nous avons ajouté des sliders interactifs afin de pouvoir visualiser les différentes tranches.

Nous avons 3 sliders et donc 3 images :
- Fixed image : image de base sans recalage
- Moving image : image sur laquelle on veut se recaler
- Transformed image : image recalée

Voici donc plusieurs exemples de ces images :

![](md_images/recalage_88.png)
![](md_images/recalage_2.png)
![](md_images/recalage_36.png)

## Segmentation

### Approche initiale: segmentation par seuillage automatique

Dans un premier temps, nous avons implémenté une segmentation par seuillage automatique. Cependant, nous nous sommes confrontés à un problème : l'API n'était pas assez complète pour nous permettre de faire une segmentation automatique et depasser les problemes d'execution rencontres.

Pour gagner du temps, nous avons donc décidé de nous diriger vers une autre approche.

### Approche finale: segmentation par seuillage manuel

L'approche finalement utilisée est une segmentation par seuillage manuel. En effet, avec ce type de segmentation, nous avons pu contourner les problèmes d'API puisque l'utilisation de la fonction itk.ConnectedThresholdImageFilter a fonctionne sans problème.

Il a fallu choisir un seuil par axe (x, y, z) afin de pouvoir segmenter correctement l'image. Voici le résultat obtenu :

![](md_images/segmentation.png)

Il a fallu ensuite selectionne les tranches qui nous intéressaient afin de pouvoir les afficher. et detourer la tumeur une fois identifiee. Voici le résultat obtenu :

![](md_images/segmentation2.png)
![](md_images/segmentation3.png)

