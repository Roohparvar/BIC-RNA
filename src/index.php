<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $rna_sequence = htmlspecialchars($_POST['rna_sequence']);
    $user_email = htmlspecialchars($_POST['user_email']);
} else {
    header("Location: index.html");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
			background-blend-mode: color-burn;
			background-size: 150px;
        }
        .result-container {
            padding: 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<div class="result-container">
    <h2>Result</h2>
    <p><strong>RNA Sequence:</strong> <?php echo $rna_sequence; ?></p>
    <p><strong>Email:</strong> <?php echo $user_email; ?></p>
</div>

</body>
</html>
