import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
    insecureSkipTLSVerify: true, // Esta opción deshabilita la verificación del certificado
    stages: [
        { duration: '1s', target: 100 },  // Simulate ramp-up of traffic from 0 to 100 users over 1 second.
        { duration: '8s', target: 100 },  // Stay at 100 users for 8 seconds.
        { duration: '1s', target: 0 },    // Ramp-down to 0 users over 1 second.
    ],
};

export default function () {
    let url = 'https://ms1.client.localhost/api/v1/client/create';
    let payload = JSON.stringify({
        name: "juan",
        surname: "perez",
        phone_number: "123456789",
        email: "juanperez@gmail.com",
        dni: "12345678",
        address: "calle falsa 123",
        password: "12345678"
    });

    let params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    let res = http.post(url, payload, params);

    check(res, {
        'is status 200': (r) => r.status === 201,
        'response time < 500ms': (r) => r.timings.duration < 500,
    });

    sleep(0.1); // Adjust sleep to increase the number of requests per user
}

