# Digital Image Processing Intensity Transformations

## Description
This project includes implementation of some intensity transformations in Digital Image Processing for 8-bit images:
- Linear transformation: $f(i) = \alpha i + \beta$ (custom $\alpha$ and $\beta$)
- Negative transformation: $f(i) = -i + 255$ (a special case of linear transformation)
- Piecewise linear transformation (with 2 custom transformation function breaking points)
- Logarithmic transformation: $f(i) = [\frac{255\ log(i+1)}{log(256)}]$
- Power-law transformation: $f(i) = [ci^\gamma]$ (custom $\gamma$ and calculated appropriate $c$)
- Histogram equalization

## Usage
1. set "img_path" variable in "main.py" to input image's path. (Images will be converted to grayscale.)
2. Execute the python file corresponding to transformation of choice.
    - Linear transformation: "linear.py"
    - Negative transformation: "negative.py"
    - Piecewise linear transformation: "piecewise_linear.py"
    - Logarithmic transformation: "logarithmic.py"
    - Power-law transformation: "power_law.py"
    - Histogram equalization: "histogram_equalization.py"
3. Enter requested custom parameters if necessary.
4. Transformed output image will be shown.


## Sample Outputs
### Grayscale input:
![Cute Piglet](assets/images/grayscale.png)

### Linear transformation ($\alpha=2, \beta=50$):
![Cute Piglet linear transformation alpha=2 beta=50](assets/images/linear_alpha2_beta50.png)

### Negative transformation:
![Cute Piglet negative transformation](assets/images/negative.png)

### Piecewise linear transformation $((a_1, b_1) = (75, 100), (a_2, b_2) = (225, 250))$:
![Cute Piglet piecewise linear transformation a1, b1 = 75, 100 / a2, b2 = 225, 250](assets/images/piecewise_75_100_225_250.png)

### Logarithmic transformation:
![Cute Piglet logarithmic transformation](assets/images/log.png)

### Power-law transformation ($\gamma = 4$):
![Cute Piglet power-law transformation gamma=4](assets/images/power_law_gamma4.png)

### Histogram equalization:
![Cute Piglet histogram equalization](assets/images/histogram_equalization.png)


## Attributions
Sample image:
<figure>
  <img src="https://github.com/Delaram-M/intensity-transformation/blob/main/assets/images/cute-piglet.jpg" alt="Cute Piglet" width="250"> 
  <figcaption>
     <a href="https://www.publicdomainpictures.net/en/view-image.php?image=24588&picture=cute-piglet">Cute Piglet</a> 
     by <a href="https://www.publicdomainpictures.net/en/browse-author.php?a=1">Petr Kratochvil</a> 
     is licensed under <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a>.
  </figcaption>
</figure>
