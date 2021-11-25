<?php
//codewars.com/kata/5592e3bd57b64d00f3000047/php
//Remove PHP opening and closing tag in order to parse it correctly on codewars.com
function findNb($m) 
{
  $v = 0;
  $n = 0;
  while ($m > $v)
    $v += $n++**3;
  return $v == $m ? $n-1 : -1;
}
?>
