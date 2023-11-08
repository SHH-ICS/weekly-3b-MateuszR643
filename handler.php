<!DOCTYPE HTML>
<html>
  <head>
    <link rel="apple-touch-icon" sizes="180x180" href="favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicons/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="512x512" href="favicons/android-chrome-512x512.png">
    <link rel="icon" type="image/png" sizes="192x192" href="favicons/android-chrome-192x192.png">
    <link rel="manifest" href="favicons/site.webmanifest">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <link rel="stylesheet" href="./css/styles.css">
    <title>Dezmond's Pizzeria</title>
  </head>

  <body class="body">
    <h1 class="header">Dezmond's Pizzeria</h1>

    <?php
    $size = "";
    $toppings = "";
    $pizzaprices = [6.00, 10.00];
    $topprices = [0.00, 1.00, 1.75, 2.50, 3.35];

    if ( isset( $_POST['size']) and isset( $_POST['toppings'])) {
      $myVariable = $_POST['size'];
      $myVariable = $_POST['toppings'];
      $tax = $pizzaprices[$size - 1] * 0.13 + $topprices[$topprices - 0] * 0.13;
      $price = $pizzaprices[$size - 1] + $topprices[$topprices - 0] + $tax;
      echo "<p class=\"paragraph\">You ordered item ".$size." and ".$toppings." toppings
      \n Your total is: $".$price.
      "\n Thank you for ordering from Dezmond's Pizzeria</p>";
    }
    else {
      echo "<h1 class=\"header\">Please input a complete order.</h1>";
    }
    ?>
    
  </body>
  
</html>
