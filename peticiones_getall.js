import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  insecureSkipTLSVerify: true,
  vus: 100, // número de usuarios virtuales
  iterations: 100, // número de iteraciones totales (peticiones)
};

export default function () {
  let res = http.get('https://ms1.client.localhost/api/v1/client/all');
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
}

