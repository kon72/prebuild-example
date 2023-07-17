import {bindings} from './binding';

test('Exposes hello function', () => {
  expect(typeof bindings.hello).toBe('function');
  expect(bindings.hello()).toBe('Hello from C++');
});
