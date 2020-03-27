<?php 

function tree(&$arr_file, $directory, $dir_name='') 
{
    $mydir = dir($directory);
    while($file = $mydir->read())
    {
        if((is_dir("$directory/$file")) AND ($file != ".") AND ($file != ".."))
        {
            tree($arr_file, "$directory/$file", "$dir_name/$file");
        }
        else if(($file != ".") AND ($file != ".."))
        {
            $arr_file[] = "$dir_name/$file";
        }
    }
    $mydir->close();
}
//开始运行
$arr_file = array();
tree($arr_file, $dir);
print_r($arr_file);


//递归方式  
function read_dir($dir){  
    $files=array();  
    $dir_list=scandir($dir);  
    foreach($dir_list as $file){  
        if($file!='..' && $file!='.'){  
            if(is_dir($dir.'/'.$file)){  
                $files[]=read_dir($dir.'/'.$file);  
            }else{  
                $files[]=$file;  
            }  
        }  
    }  
    return $files;  
}  
//队列方式   
function read_dir_queue($dir){  
    $files=array();  
    $queue=array($dir);  
    while($data=each($queue)){  
        $path=$data['value'];  
        if(is_dir($path) && $handle=opendir($path)){  
            while($file=readdir($handle)){  
                if($file=='.'||$file=='..') continue;  
                $files[] = $real_path=$path.'/'.$file;  
                if (is_dir($real_path)) $queue[] = $real_path;  
            }  
        }  
        closedir($handle);  
    }  
     return $files;  
}  