const sum = require('./sum');

test('dodaje 1 + 2, wynik to 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('dodaje -1 + 1, wynik to 0', () => {
  expect(sum(-1, 1)).toBe(0);
});

test('dodaje -1 + -1, wynik to -2', () => {
  expect(sum(-1, -1)).toBe(-2);
});
