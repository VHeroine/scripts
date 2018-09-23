function factorial(num) {
	if (num == 0 || num == 1) return 1;
	num = num * factorial(num - 1);
	return num;
}

function append_value(ap_value, to_add) {
document.getElementById(to_add).value += ap_value;
return null;
}

function fib_seq(num) {
	if (num == 0) return 0;
	var a = 1, b = 1, i = 1, sum = 0;
	while (i < num) {
		sum = a + b;
		a = b;
		b = sum;
		i++;
	}
	return a;
}