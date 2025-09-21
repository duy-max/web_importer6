// login.test.ts
import { sleep, check } from "k6";
import { config } from "../k6config";
import { login } from "../utils";

export const options = config.options;

export function loginTest () {
  const token = login(config.BASE_URL, config.IDENTIFIER, config.PASSWORD);

  const ok = check(token, {
    "got token": (t) => t !== null,
  });

  if (!ok) {
    console.error(
      JSON.stringify({
        url: `${config.BASE_URL}/api/auth/local`,
        status: "failed",
        message: "Login failed, no token returned",
      })
    );
  }

  sleep(1);
}

// K6 hook để ghi báo cáo cuối cùng
// export function handleSummary(data: any) {
//   return {
//     "result.json": JSON.stringify(data, null, 2), // full report
//   };
// }
