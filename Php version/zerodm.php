<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <title>Zero����URL��ȡ</title>
    <link rel="stylesheet" type="text/css" href="common.css" />
  </head>
  <body>
    <h1>����zero������վ����ѯѸ�����ص�ַ</h1>
<?php
displayForm();
if ( isset( $_POST["submitted"] ) ) {
  processForm();
}
 
function displayForm() {
?>
<h2>����Ŀ¼ҳ�棬����http://dmxz.zerodm.net/xiazai/XXXX.html��</h2>
    <form action="" method="post" style="width: 30em;">
      <div>
        <input type="hidden" name="submitted" value="1" />
        <label for="url">URL:</label>
        <input type="text" name="url" id="url" value="" />
        <label> </label>
        <input type="submit" name="submitButton" value="��ѯ" />
      </div>
    </form>
<?php
}
 
function processForm() {
  $url = $_POST["url"];
  if ( !preg_match( '|^http(s)?\://|', $url ) ) $url = "http://$url";
  $html = file_get_contents( $url );
  preg_match_all( "/<a\s*href=['\"](.+?xunlei.+?)['\"].*?>/i", 
                  $html, $matches );
 
  echo '<div style="clear: both;"> </div>';
  echo "<h2>����" . htmlspecialchars( $url ) . "��Ŀ����������:</h2>";
   
  echo "<ul style='word-break: break-word;'>";
   
  for ( $i = 0; $i < count( $matches[1] ); $i++ ) {
   $xunleiurl = file_get_contents($matches[1][$i]);
   preg_match_all( "/href=['\"](http.+?sendfile.+?)['\"].*?>/i",
                   $xunleiurl , $urlmatches );
   for ( $k = 0; $k < count( $urlmatches[1] ); $k++ ) {
    echo "<li>" . htmlspecialchars( $urlmatches[1][$k] ) . "</li>";
  }
  }
  echo "</ul>";
}
 
?>
  </body>
</html>