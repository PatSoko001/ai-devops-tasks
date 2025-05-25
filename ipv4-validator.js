function isValidIPv4(ip) {
  const ipv4Regex = /^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$/;
  return ipv4Regex.test(ip);
}

// Przykładowe użycie:
console.log(isValidIPv4("192.168.1.1"));     // true
console.log(isValidIPv4("255.255.255.255")); // true
console.log(isValidIPv4("0.0.0.0"));         // true
console.log(isValidIPv4("256.100.50.0"));    // false
console.log(isValidIPv4("192.168.1"));       // false
console.log(isValidIPv4("abc.def.ghi.jkl")); // false
