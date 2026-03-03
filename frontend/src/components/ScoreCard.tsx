import { cn } from "@/lib/utils";
import { ScoreBar, getScoreTextColor } from "./ScoreBar";

interface ScoreCardProps {
  icon: string;
  title: string;
  score: number;
  items: { label: string; score: number }[];
  note?: string;
}

const ScoreCard = ({ icon, title, score, items, note }: ScoreCardProps) => (
  <div className="rounded-lg border border-border bg-card p-5 flex flex-col gap-4">
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-2">
        <span className="text-xl">{icon}</span>
        <h3 className="font-semibold text-card-foreground">{title}</h3>
      </div>
      <span className={cn("font-mono text-2xl font-bold", getScoreTextColor(score))}>
        {score}
      </span>
    </div>
    {note && (
      <p className="text-xs text-muted-foreground -mt-2 italic">{note}</p>
    )}
    <div className="flex flex-col gap-2.5">
      {items.map((item) => (
        <ScoreBar key={item.label} label={item.label} score={item.score} />
      ))}
    </div>
  </div>
);

export default ScoreCard;
