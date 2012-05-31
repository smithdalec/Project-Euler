<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title></title>
  </head>
  <body>
    <?php
// look in current directory
$files = scandir('.');
$ignored_files = array(
  '.',
  '..',
  '.git',
  'index.php',
  'krumo',
  'nbproject',
);
// not an actual directory, but the location of the MAMP page
foreach ($files as $file) {
	// exclude elements in the array containing a period (files and hidden folders)
	if (!in_array($file, $ignored_files))
		echo '<a href=' . $file . '>' . $file .  '</a><br/>';
}
?>
  </body>
</html>
