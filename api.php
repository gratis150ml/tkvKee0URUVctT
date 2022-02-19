<?php
header("Content-Type:application/json");
if(!empty($_GET['username'])) {
    $username = $_GET['username']
    $logs = get_logs($username);
    if(empty($logs)){
        response()
    }
}
?>