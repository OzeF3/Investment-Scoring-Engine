import { cn } from "@/lib/utils";

interface FinalScoreProps {
  score: number;
  companyName: string;
  ticker: string;
  sector: string;
}

const getScoreGradient = (score: number) => {
  if (score <= 40) return "from-score-red/20 to-score-red/5 border-score-red/30";
  if (score <= 65) return "from-score-yellow/20 to-score-yellow/5 border-score-yellow/30";
  return "from-score-green/20 to-score-green/5 border-score-green/30";
};

const getScoreText = (score: number) => {
  if (score <= 40) return "text-score-red";
  if (score <= 65) return "text-score-yellow";
  return "text-score-green";
};

const getScoreLabel = (score: number) => {
  if (score <= 40) return "Weak";
  if (score <= 65) return "Fair";
  if (score <= 80) return "Strong";
  return "Excellent";
};

const FinalScore = ({ score, companyName, ticker, sector }: FinalScoreProps) => (
  <div className="text-center space-y-4">
    <div className="space-y-1">
      <h1 className="text-3xl font-bold text-foreground tracking-tight">
        {companyName}
      </h1>
      <div className="flex items-center justify-center gap-3 text-muted-foreground">
        <span className="font-mono text-primary font-semibold">{ticker}</span>
        <span className="text-border">•</span>
        <span className="text-sm">{sector}</span>
      </div>
    </div>
    <div
      className={cn(
        "inline-flex flex-col items-center rounded-xl border bg-gradient-to-b px-10 py-6",
        getScoreGradient(score)
      )}
    >
      <span className="text-xs uppercase tracking-widest text-muted-foreground mb-1">
        Overall Score
      </span>
      <span className={cn("font-mono text-6xl font-bold", getScoreText(score))}>
        {score}
      </span>
      <span className={cn("text-sm font-medium mt-1", getScoreText(score))}>
        {getScoreLabel(score)}
      </span>
    </div>
  </div>
);

export default FinalScore;
