codewars.com/kata/5592e3bd57b64d00f3000047/php
function findNb($m) 
{
  $v = 0;
  $n = 0;
  while ($m > $v)
    $v += $n++**3;
  return $v == $m ? $n-1 : -1;
}
