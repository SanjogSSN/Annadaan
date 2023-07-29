// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your Javascript code.

// Food Bank Registration Validation
function fbValidate()
{
    var x = document.forms["FBForm"]["num"].value;
    var y = document.forms["FBForm"]["loc"].value;
    var z = document.forms["FBForm"]["iname"].value;
    if(/^[2-9]{1}[0-9]{9}$/.test(x) == false)
    {
        alert("Invalid Number!");
		return false;
    }
    if(/^[a-z0-9\s,'-]*$/i.test(y) == false)
    {
        alert("Invalid Address!");
		return false;
    }
    if(/^[A-Za-z\s]+$/.test(z) == false)
    {
        alert("Invalid Incharge Name!");
		return false;
    }
    document.FBForm.submit();
}

// Volunteer Registration Validation

function volunteerVal()
{
    var a = document.forms["volunteer"]["fname"].value;
    var b = document.forms["volunteer"]["address"].value;
    var c = document.forms["volunteer"]["email"].value;
    var d = document.forms["volunteer"]["num"].value;
    var e = document.forms["volunteer"]["pass"].value;
    var f = document.forms["volunteer"]["rpass"].value;
    var g = document.getElementsByName('radio');
	var em = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    
    if((a=="")||(b=="")||(c=="")||(d=="")||(e=="")||(f==""))
    {
        alert("Please enter all the details!");
        return false;
    }
    if(/^[A-Za-z\s]+$/.test(a) == false)
    {
        alert("Invalid Name!");
		return false;
    }
    if(/^[a-z0-9\s,'-]*$/i.test(b) == false)
    {
        alert("Invalid Address!");
		return false;
    }
    if(em.test(c) == false)
    {
        alert("Invalid Email!");
		return false;
    }
    if(/^[2-9]{1}[0-9]{9}$/.test(d) == false)
    {
        alert("Invalid Number!");
		return false;
    }
    if(e.length < 8 || e.length > 15)
    {
        alert("Password length must be from 8 to 15!");
		return false;
    }
    if(!(e == f))
    {
        alert("Password doesn't match!");
		return false;
    }
    if (!(g[0].checked || g[1].checked))
    {
        alert("Please Select an Option");
        return false;
    }
    document.volunteer.submit();
}

// Donation Request Validation

function requestVal()
{
    var a = document.forms["ReqForm"]["fi"].value;
    var b = document.forms["ReqForm"]["qty"].value;
    var c = document.forms["ReqForm"]["loc"].value;
    var d = document.forms["ReqForm"]["num"].value;
    
    if((a=="")||(b=="")||(c=="")||(d==""))
    {
        alert("Please enter all the details!");
        return false;
    }
    if(a < 0)
    {
        alert("Please enter a valid number!");
		return false;
    }
    if(/^[0-9]+$/.test(b) == false)
    {
        alert("Please enter a valid quantity!");
		return false;
    }
    if(/^[a-z0-9\s,'-]*$/i.test(c) == false)
    {
        alert("Invalid Location!");
		return false;
    }
    if(/^[2-9]{1}[0-9]{9}$/.test(d) == false)
    {
        alert("Invalid Number!");
		return false;
    }
    document.ReqForm.submit();
}

// Show Password

function showpass()
{
    var x = document.getElementById("psw");
    if (x.type === "password")
        x.type = "text";
    else
        x.type = "password";
}

// Feedback

function msg()
{
	document.getElementById("e1").innerHTML = "";
	document.getElementById("e2").innerHTML = "";
	var n = document.forms["DUAM"]["name"].value;
	var e = document.forms["DUAM"]["email"].value;
	var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

	if(n==""){
		alert("Name is required!");
		return false;
	}
	if(e==""){
		alert("Email is required!");
		return false;
	}
	if (reg.test(e) == false){
		alert("Please enter a valid email id!");
        return false;
	}
	if(!(n="")||(e=="")){
		document.DUAM.submit();
	}
}