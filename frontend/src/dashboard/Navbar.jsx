import React, { useState } from "react";
import {
  LayoutDashboard,
  Send,
  Zap,
  Users,
  FileText,
  Settings,
  Search,
  Bell,
  ChevronRight,
  MoreHorizontal,
  ArrowUpRight,
  ArrowDownRight,
  Mail,
  Inbox,
  CheckCircle2,
  Clock,
} from "lucide-react";
import {
  AreaChart,
  Area,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

// ---------------------------------------------------------------------------
// Design tokens
// Palette:  #FFFFFF white surface · #F6F8FC app background · #0F1E3D navy
//           (sidebar / headline ink) · #2563EB primary blue · #EFF4FF
//           soft-blue tint · #E4E9F2 hairline border · #64748B secondary text
// Type:     Space Grotesk (display) · Inter (body/UI) · IBM Plex Mono (data)
// ---------------------------------------------------------------------------

const chartData = [
  { day: "Mon", opens: 420, clicks: 110 },
  { day: "Tue", opens: 512, clicks: 148 },
  { day: "Wed", opens: 478, clicks: 132 },
  { day: "Thu", opens: 610, clicks: 190 },
  { day: "Fri", opens: 705, clicks: 224 },
  { day: "Sat", opens: 388, clicks: 96 },
  { day: "Sun", opens: 344, clicks: 84 },
];

const navItems = [
  { label: "Dashboard", icon: LayoutDashboard, active: true },
  { label: "Campaigns", icon: Send },
  { label: "Automations", icon: Zap },
  { label: "Contacts", icon: Users },
  { label: "Templates", icon: FileText },
  { label: "Settings", icon: Settings },
];

const pipeline = [
  { stage: "Triggered", count: 1240, icon: Zap },
  { stage: "Queued", count: 386, icon: Clock },
  { stage: "Sending", count: 92, icon: Inbox },
  { stage: "Delivered", count: 11284, icon: CheckCircle2 },
];

const automations = [
  { name: "Welcome series", trigger: "New signup", status: "Running", sent: "3,204" },
  { name: "Cart abandonment", trigger: "Cart idle 2h", status: "Running", sent: "1,118" },
  { name: "Re-engagement", trigger: "Inactive 30d", status: "Paused", sent: "842" },
  { name: "Post-purchase follow-up", trigger: "Order delivered", status: "Running", sent: "2,566" },
];

const campaigns = [
  { name: "July product update", status: "Sent", sent: "18,204", opens: "42.1%", clicks: "9.8%", date: "Jun 28" },
  { name: "Summer sale — 48h only", status: "Sent", sent: "24,910", opens: "38.6%", clicks: "12.3%", date: "Jun 24" },
  { name: "New feature: smart replies", status: "Scheduled", sent: "—", opens: "—", clicks: "—", date: "Jul 5" },
  { name: "Customer story: Halden Co.", status: "Draft", sent: "—", opens: "—", clicks: "—", date: "—" },
];

function StatusPill({ status }) {
  const styles = {
    Running: "bg-[#EFF4FF] text-[#2563EB]",
    Sent: "bg-[#EFF4FF] text-[#2563EB]",
    Paused: "bg-[#F1F5F9] text-[#64748B]",
    Scheduled: "bg-[#FEF3E8] text-[#C2680A]",
    Draft: "bg-[#F1F5F9] text-[#64748B]",
  };
  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-xs font-medium ${styles[status] || "bg-slate-100 text-slate-500"}`}
    >
      <span className="h-1.5 w-1.5 rounded-full bg-current opacity-70" />
      {status}
    </span>
  );
}

function StatCard({ label, value, delta, up, icon: Icon }) {
  return (
    <div className="rounded-2xl border border-[#E4E9F2] bg-white p-5">
      <div className="flex items-center justify-between">
        <span className="text-sm text-[#64748B]">{label}</span>
        <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-[#EFF4FF] text-[#2563EB]">
          <Icon size={16} strokeWidth={2} />
        </div>
      </div>
      <div className="mt-4 flex items-end justify-between">
        <span
          className="text-3xl font-semibold tracking-tight text-[#0F1E3D]"
          style={{ fontFamily: "'Space Grotesk', sans-serif" }}
        >
          {value}
        </span>
        <span
          className={`flex items-center gap-0.5 text-xs font-medium ${up ? "text-[#2563EB]" : "text-[#94A3B8]"}`}
        >
          {up ? <ArrowUpRight size={13} /> : <ArrowDownRight size={13} />}
          {delta}
        </span>
      </div>
    </div>
  );
}

export default function EmailDashboard() {
  const [active, setActive] = useState("Dashboard");
  const totalPipeline = pipeline.reduce((a, b) => a + b.count, 0);

  return (
    <div
      className="flex h-full min-h-[760px] w-full bg-[#F6F8FC] text-[#1E293B]"
      style={{ fontFamily: "'Inter', sans-serif" }}
    >
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap');
      `}</style>

      {/* Sidebar */}
      <aside className="hidden w-64 flex-col bg-[#0F1E3D] px-4 py-6 md:flex">
        <div className="flex items-center gap-2 px-2">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-[#2563EB]">
            <Mail size={16} className="text-white" strokeWidth={2.2} />
          </div>
          <span
            className="text-lg font-semibold text-white"
            style={{ fontFamily: "'Space Grotesk', sans-serif" }}
          >
            Relay
          </span>
        </div>

        <nav className="mt-8 flex flex-1 flex-col gap-1">
          {navItems.map(({ label, icon: Icon }) => {
            const isActive = active === label;
            return (
              <button
                key={label}
                onClick={() => setActive(label)}
                className={`flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm transition-colors ${
                  isActive
                    ? "bg-white/10 text-white font-medium"
                    : "text-[#94A3B8] hover:bg-white/5 hover:text-white"
                }`}
              >
                <Icon size={17} strokeWidth={2} />
                {label}
              </button>
            );
          })}
        </nav>

        <div className="rounded-xl bg-white/5 p-4">
          <p className="text-xs text-[#94A3B8]">Monthly sends</p>
          <p className="mt-1 text-sm font-medium text-white">42,180 / 60,000</p>
          <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-white/10">
            <div className="h-full w-[70%] rounded-full bg-[#2563EB]" />
          </div>
        </div>
      </aside>

      {/* Main */}
      <div className="flex flex-1 flex-col overflow-y-auto">
        {/* Topbar */}
        <header className="flex items-center justify-between border-b border-[#E4E9F2] bg-white px-8 py-5">
          <div>
            <h1
              className="text-xl font-semibold text-[#0F1E3D]"
              style={{ fontFamily: "'Space Grotesk', sans-serif" }}
            >
              Dashboard
            </h1>
            <p className="text-sm text-[#64748B]">Thursday, July 2 — here's how your emails are performing.</p>
          </div>
          <div className="flex items-center gap-3">
            <div className="hidden items-center gap-2 rounded-lg border border-[#E4E9F2] bg-[#F6F8FC] px-3 py-2 sm:flex">
              <Search size={15} className="text-[#94A3B8]" />
              <input
                placeholder="Search campaigns..."
                className="w-40 bg-transparent text-sm text-[#1E293B] placeholder:text-[#94A3B8] focus:outline-none"
              />
            </div>
            <button className="relative flex h-9 w-9 items-center justify-center rounded-lg border border-[#E4E9F2] text-[#64748B] hover:bg-[#F6F8FC]">
              <Bell size={16} />
              <span className="absolute right-2 top-2 h-1.5 w-1.5 rounded-full bg-[#2563EB]" />
            </button>
            <div className="flex h-9 w-9 items-center justify-center rounded-full bg-[#EFF4FF] text-sm font-medium text-[#2563EB]">
              JM
            </div>
          </div>
        </header>

        <main className="flex-1 space-y-6 px-8 py-6">
          {/* Stat cards */}
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <StatCard label="Emails sent" value="60.2k" delta="12.4%" up icon={Send} />
            <StatCard label="Open rate" value="41.8%" delta="3.1%" up icon={Inbox} />
            <StatCard label="Click rate" value="11.6%" delta="0.6%" up={false} icon={ArrowUpRight} />
            <StatCard label="Active automations" value="9" delta="2 new" up icon={Zap} />
          </div>

          {/* Signature: automation pipeline */}
          <div className="rounded-2xl border border-[#E4E9F2] bg-white p-6">
            <div className="mb-5 flex items-center justify-between">
              <div>
                <h2
                  className="text-base font-semibold text-[#0F1E3D]"
                  style={{ fontFamily: "'Space Grotesk', sans-serif" }}
                >
                  Automation pipeline
                </h2>
                <p className="text-sm text-[#64748B]">Live status of messages moving through your flows</p>
              </div>
              <span
                className="rounded-full bg-[#EFF4FF] px-3 py-1 text-xs font-medium text-[#2563EB]"
                style={{ fontFamily: "'IBM Plex Mono', monospace" }}
              >
                {totalPipeline.toLocaleString()} total
              </span>
            </div>

            {/* segmented flow bar */}
            <div className="flex h-2.5 w-full overflow-hidden rounded-full bg-[#F1F5F9]">
              {pipeline.map((p, i) => (
                <div
                  key={p.stage}
                  className="h-full"
                  style={{
                    width: `${(p.count / totalPipeline) * 100}%`,
                    backgroundColor: ["#93B4F5", "#5F8CF0", "#2563EB", "#0F1E3D"][i],
                  }}
                />
              ))}
            </div>

            <div className="mt-5 grid grid-cols-2 gap-4 sm:grid-cols-4">
              {pipeline.map((p, i) => (
                <div key={p.stage} className="flex items-start gap-3">
                  <div
                    className="mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg"
                    style={{
                      backgroundColor: ["#93B4F5", "#5F8CF0", "#2563EB", "#0F1E3D"][i] + "22",
                      color: ["#93B4F5", "#5F8CF0", "#2563EB", "#0F1E3D"][i],
                    }}
                  >
                    <p.icon size={15} strokeWidth={2} />
                  </div>
                  <div>
                    <p className="text-xs text-[#64748B]">{p.stage}</p>
                    <p
                      className="text-sm font-semibold text-[#0F1E3D]"
                      style={{ fontFamily: "'IBM Plex Mono', monospace" }}
                    >
                      {p.count.toLocaleString()}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Chart + automations list */}
          <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
            <div className="rounded-2xl border border-[#E4E9F2] bg-white p-6 lg:col-span-2">
              <div className="mb-4 flex items-center justify-between">
                <h2
                  className="text-base font-semibold text-[#0F1E3D]"
                  style={{ fontFamily: "'Space Grotesk', sans-serif" }}
                >
                  Engagement, last 7 days
                </h2>
                <div className="flex items-center gap-4 text-xs text-[#64748B]">
                  <span className="flex items-center gap-1.5">
                    <span className="h-2 w-2 rounded-full bg-[#2563EB]" /> Opens
                  </span>
                  <span className="flex items-center gap-1.5">
                    <span className="h-2 w-2 rounded-full bg-[#B9CDF7]" /> Clicks
                  </span>
                </div>
              </div>
              <div className="h-56">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={chartData} margin={{ top: 5, right: 5, left: -20, bottom: 0 }}>
                    <defs>
                      <linearGradient id="opensFill" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stopColor="#2563EB" stopOpacity={0.22} />
                        <stop offset="100%" stopColor="#2563EB" stopOpacity={0} />
                      </linearGradient>
                    </defs>
                    <CartesianGrid vertical={false} stroke="#EEF2F8" />
                    <XAxis
                      dataKey="day"
                      axisLine={false}
                      tickLine={false}
                      tick={{ fill: "#94A3B8", fontSize: 12 }}
                    />
                    <YAxis axisLine={false} tickLine={false} tick={{ fill: "#94A3B8", fontSize: 12 }} />
                    <Tooltip
                      contentStyle={{
                        borderRadius: 10,
                        border: "1px solid #E4E9F2",
                        fontSize: 12,
                        fontFamily: "Inter, sans-serif",
                      }}
                    />
                    <Area
                      type="monotone"
                      dataKey="opens"
                      stroke="#2563EB"
                      strokeWidth={2}
                      fill="url(#opensFill)"
                    />
                    <Area
                      type="monotone"
                      dataKey="clicks"
                      stroke="#B9CDF7"
                      strokeWidth={2}
                      fill="transparent"
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="rounded-2xl border border-[#E4E9F2] bg-white p-6">
              <div className="mb-4 flex items-center justify-between">
                <h2
                  className="text-base font-semibold text-[#0F1E3D]"
                  style={{ fontFamily: "'Space Grotesk', sans-serif" }}
                >
                  Automations
                </h2>
                <button className="text-[#94A3B8] hover:text-[#64748B]">
                  <MoreHorizontal size={16} />
                </button>
              </div>
              <ul className="space-y-4">
                {automations.map((a) => (
                  <li key={a.name} className="flex items-start justify-between gap-3">
                    <div className="min-w-0">
                      <p className="truncate text-sm font-medium text-[#0F1E3D]">{a.name}</p>
                      <p className="text-xs text-[#64748B]">{a.trigger}</p>
                    </div>
                    <StatusPill status={a.status} />
                  </li>
                ))}
              </ul>
              <button className="mt-5 flex w-full items-center justify-center gap-1 rounded-lg border border-[#E4E9F2] py-2 text-sm font-medium text-[#2563EB] hover:bg-[#EFF4FF]">
                View all automations <ChevronRight size={14} />
              </button>
            </div>
          </div>

          {/* Campaigns table */}
          <div className="rounded-2xl border border-[#E4E9F2] bg-white p-6">
            <div className="mb-4 flex items-center justify-between">
              <h2
                className="text-base font-semibold text-[#0F1E3D]"
                style={{ fontFamily: "'Space Grotesk', sans-serif" }}
              >
                Recent campaigns
              </h2>
              <button className="rounded-lg bg-[#2563EB] px-4 py-2 text-sm font-medium text-white hover:bg-[#1D4ED8]">
                New campaign
              </button>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="border-b border-[#E4E9F2] text-xs text-[#94A3B8]">
                    <th className="py-2 font-medium">Campaign</th>
                    <th className="py-2 font-medium">Status</th>
                    <th className="py-2 font-medium">Sent</th>
                    <th className="py-2 font-medium">Opens</th>
                    <th className="py-2 font-medium">Clicks</th>
                    <th className="py-2 font-medium">Date</th>
                  </tr>
                </thead>
                <tbody>
                  {campaigns.map((c) => (
                    <tr key={c.name} className="border-b border-[#F1F5F9] last:border-0">
                      <td className="py-3.5 font-medium text-[#0F1E3D]">{c.name}</td>
                      <td className="py-3.5">
                        <StatusPill status={c.status} />
                      </td>
                      <td
                        className="py-3.5 text-[#64748B]"
                        style={{ fontFamily: "'IBM Plex Mono', monospace" }}
                      >
                        {c.sent}
                      </td>
                      <td
                        className="py-3.5 text-[#64748B]"
                        style={{ fontFamily: "'IBM Plex Mono', monospace" }}
                      >
                        {c.opens}
                      </td>
                      <td
                        className="py-3.5 text-[#64748B]"
                        style={{ fontFamily: "'IBM Plex Mono', monospace" }}
                      >
                        {c.clicks}
                      </td>
                      <td className="py-3.5 text-[#64748B]">{c.date}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}