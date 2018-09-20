function factorial(num) {
	if (num == 0 || num == 1) return 1;
	num = num * factorial(num - 1);
	return num;
}

function append_value(ap_value, to_add) {
document.getElementById(to_add).value += ap_value;
return null;
}