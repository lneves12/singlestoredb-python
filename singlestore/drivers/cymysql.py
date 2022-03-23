from __future__ import annotations

from typing import Any
from typing import Dict

from .base import Driver


class CyMySQLDriver(Driver):

    name = 'CyMySQL'

    pkg_name = 'cymysql'
    pypi = 'cymysql'
    anaconda = 'cymysql'

    def remap_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        params.pop('driver', None)
        params.pop('pure_python', None)
        params.pop('odbc_driver', None)
        params['port'] = params['port'] or 3306
        params['db'] = params.pop('database')
        params['passwd'] = params.pop('password')
        if params['raw_values']:
            params['conv'] = {}
        params.pop('raw_values', None)
        return params
