// JavaScript Document
		function loginClick() {
			var name = document.login.username.value;
			var pwd = document.login.password.value;
			if (name == null || name.length == 0) {
				alert("用户名不能为空！");
				return;
			}
			if (pwd == null || pwd.length == 0) {
				alert("密码不能为空！");
				return;
			}
			document.login.submit();

		}

function registerClick() {
	var r_name = document.register.username.value;
	var r_pwd = document.register.password.value;
	if (r_name == null || r_name.length == 0) {
		alert("用户名不能为空！");
		return;
	}
	if (r_pwd == null || r_pwd.length < 8) {
		alert("密码位数不能小于8位！");
		return;
	}
	document.register.submit();
}
