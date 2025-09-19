import http from "k6/http";
import { sleep, check } from "k6";

export const options = {
  scenarios: {
    login_smoke: {
      executor: "constant-vus",
      vus: 5,
      duration: "30s",
    },
  },
  thresholds: {
    "http_req_duration{endpoint:login}": ["p(95)<1000"],   // 95% < 1s
    "checks{endpoint:login}": ["rate>0.95"],               // >= 95% check pass
  },
};

const BASE_URL = __ENV.K6_BASE_URL || "https://importers.cartek.com.vn";
const IDENTIFIER = __ENV.IDENTIFIER || "qcteam.rdhw@vn.innova.com";
const PASSWORD = __ENV.PASSWORD || "qcteam.rdhw";

export default function () {
  const url = `${BASE_URL}/api/auth/local`;
  const payload = JSON.stringify({
    identifier: IDENTIFIER,
    password: PASSWORD,
  });

  const params = {
    headers: { "Content-Type": "application/json" },
    tags: { endpoint: "login" },
  };

  const res = http.post(url, payload, params);

  check(res, {
    "status is 200": (r) => r.status === 200,
    "is json": (r) =>
      String(r.headers["Content-Type"] || "").includes("application/json"),
    "has token/user": (r) => {
      try {
        const data = r.json() as any;
        return !!(data && (data.jwt || data.token || data.user));
      } catch {
        return false;
      }
    },
  }, { endpoint: "login" });

  sleep(1);
}