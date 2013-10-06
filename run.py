#!/usr/bin/env python
import os
from flashforward import flashforward


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	flashforward.run(host='0.0.0.0', port=port, debug=True)