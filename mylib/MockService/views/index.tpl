<!DOCTYPE html>
<html>
<style>

body{
	font-family: Arial;
	margin:0px;
    padding: 0px;


}
a{
	display:block;
    color: black;
	text-decoration: none;
    padding: 10px 10px 10px 25px;
    
}

.animate-charcter
{
  background-image: linear-gradient(117deg, #ff47b5 16%, #3aef3c 100%, #5045ea);
  background-size: auto auto;
  background-clip: border-box;
  background-size: 200% auto;
  color: #fff;
  background-clip: text;
  text-fill-color: transparent;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: textclip 2s ease infinite;
  display: block;
  font-size: 80px;
}
    

@keyframes textclip {
  to {
    background-position: 200% center;
  }
}

h1{
	background:#333;
    color:#fff;
    padding: 10px 10px 0px 5%;
	background: linear-gradient(117deg, #ff90d3 16%, #3aef3c 100%, #45ea45);
}

p{
	padding: 10px;
}

</style>
<body>
<h1 class="animate-charcter">MOCKE<small style="font-size:20px ;">ve</small>RY Service in Running</h1>
</h1>

    <h1>Welcome to <b>MockeryService</b></h1>
    <p>This is a python service designed with bottle.py to mock every WebService</p>
    <ul style="margin-left: 20px;">
        <li>Just create the folder path/folder tree next to <b>MockeryService.py</b> file [Ex <b>/department/it/team/users</b>]</li>
        <li>Place a xml/json file at the folder with some name, [Ex <b>"Sample1.xml"</b>]</li>
        <li>The first parameter name can be anything but pass the value as Sample1 [Ex <b>?Id=Sample1</b> or <b>?OpenFile=Sample1</b>]</li>
        <li>The service will match an xml or json file "Sample1.xml" or "Sample1.json" depending on the requested content type and will give response</li>
    </ul>
    <p>Example: <b>http://localhost:8080/department/it/team/users?Id=Sample1</b></p>
    <p>Here the file <b>Sample1</b> should be an <b>*.xml</b> or <b>*.json</b> file in the folder <b>/department/it/team/users</p></b>
</body>
</html>
