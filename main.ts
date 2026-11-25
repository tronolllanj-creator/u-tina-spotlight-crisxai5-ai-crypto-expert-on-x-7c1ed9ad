import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

function execute(): void {
  const baseDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
  const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  
  const inputFilePath = join(baseDir, "POST.json"); // tuned
  const outputFilePath = join(targetDir, "POST.json");

  let rawData: Buffer;
  try {
    rawData = readFileSync(inputFilePath);
  } catch (err) {
    throw new Error(`Failed to read input file: ${(err as Error).message}`);
  }

  let parsedContent: unknown;
  try {
    parsedContent = JSON.parse(rawData.toString("utf8"));
  } catch (err) {
    throw new Error(`Input content is not valid JSON: ${(err as Error).message}`);
  }

  if (
    parsedContent === null ||
    typeof parsedContent !== "object" ||
    Array.isArray(parsedContent) ||
    typeof (parsedContent as Record<string, unknown>).url !== "string"
  ) {
    throw new Error("Validation failed: JSON root must be an object containing a string 'url' property.");
  }

  try {
    mkdirSync(targetDir, { recursive: true });
  } catch (err) {
    throw new Error(`Failed to create output directory: ${(err as Error).message}`);
  }

  try {
    writeFileSync(outputFilePath, rawData);
  } catch (err) {
    throw new Error(`Failed to write output file: ${(err as Error).message}`);
  }
}

try {
  execute();
} catch (error) {
  process.stderr.write((error as Error).message + "\n");
  process.exit(1);
}
