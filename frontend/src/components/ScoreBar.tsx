import { cn } from "@/lib/utils";

interface ScoreBarProps {
  label: string;
  score: number;
  className?: string;
}

const getScoreColor = (score: number) => {
  if (score <= 40) return "bg-score-red";
  if (score <= 65) return "bg-score-yellow";
  return "bg-score-green";
};

const getScoreTextColor = (score: number) => {
  if (score <= 40) return "text-score-red";
  if (score <= 65) return "text-score-yellow";
  return "text-score-green";
};

export const ScoreBar = ({ label, score, className }: ScoreBarProps) => (
  <div className={cn("flex items-center gap-3", className)}>
    <span className="text-sm text-muted-foreground w-36 shrink-0 truncate">{label}</span>
    <div className="flex-1 h-2 rounded-full bg-secondary overflow-hidden">
      <div
        className={cn("h-full rounded-full transition-all duration-700 ease-out", getScoreColor(score))}
        style={{ width: `${score}%` }}
      />
    </div>
    <span className={cn("font-mono text-sm font-semibold w-8 text-right", getScoreTextColor(score))}>
      {score}
    </span>
  </div>
);

export { getScoreColor, getScoreTextColor };
