import * as fs from 'node:fs';
import * as path from 'node:path';
import {HelloWorldBindings} from './hello_world';

const bindingPath = path.resolve(
  path.join(__dirname, '../build/Release/hello_world_binding.node')
);

// Check if the node native addon module exists.
if (!fs.existsSync(bindingPath)) {
  throw new Error(
    `The Node.js native addon module can not be found at path: ${bindingPath}`
  );
}

// eslint-disable-next-line @typescript-eslint/no-var-requires
export const bindings: HelloWorldBindings = require(bindingPath);
