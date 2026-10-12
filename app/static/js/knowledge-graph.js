(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const SVG_NS = "http://www.w3.org/2000/svg";
  const UNIT_COLORS = {1:"#287bb5",2:"#16816c",3:"#b9772d",4:"#8058ad",5:"#b04f62"};
  let allNodes = [];
  let allEdges = [];
  let visibleNodes = [];
  let visibleEdges = [];
  let selectedId = null;
  let searchText = "";
  let pathIds = new Set();

  const escapeText = (value) => String(value ?? "");
  function el(name, attrs = {}, text = null) {
    const node = document.createElementNS(SVG_NS, name);
    Object.entries(attrs).forEach(([key,value]) => node.setAttribute(key, String(value)));
    if (text !== null) node.textContent = text;
    return node;
  }
  function safeText(value) {
    return String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  }
  async function loadGraph() {
    $("kg-count").textContent = "Loading…";
    try {
      const response = await fetch("/graph/data", {headers: {"Accept":"application/json"}});
      if (!response.ok) throw new Error("Could not load the concept catalogue.");
      const payload = await response.json();
      allNodes = payload.nodes || [];
      allEdges = payload.edges || [];
      fillPathSelects();
      renderGraph();
      if (allNodes.length) selectNode((allNodes.find(n => !n.is_anchor) || allNodes[0]).id);
    } catch (error) {
      $("kg-count").textContent = "Unavailable";
      $("kg-svg").replaceChildren(el("text",{x:600,y:360,"text-anchor":"middle",fill:"#a14d28"},error.message));
    }
  }
  function filteredData() {
    const unit = Number($("kg-unit").value);
    visibleNodes = allNodes.filter(node => (!unit || node.unit === unit));
    const ids = new Set(visibleNodes.map(n => n.id));
    visibleEdges = allEdges.filter(edge => ids.has(edge.source) && ids.has(edge.target));
  }
  function layoutNodes() {
    const unit = Number($("kg-unit").value);
    const byUnit = new Map();
    visibleNodes.forEach(node => {
      if (!byUnit.has(node.unit)) byUnit.set(node.unit, []);
      byUnit.get(node.unit).push(node);
    });
    const width = unit ? 860 : 1450;
    const columnWidth = unit ? 800 : 280;
    const leftPad = unit ? 30 : 18;
    const nodeWidth = unit ? 280 : 240;
    const nodeHeight = 54;
    const rowGap = 78;
    let maxRows = 1;
    const positions = new Map();
    const units = [...byUnit.keys()].sort((a,b)=>a-b);
    units.forEach((unitNumber, columnIndex) => {
      const list = byUnit.get(unitNumber).slice().sort((a,b)=>{
        if (a.is_anchor) return -1;
        if (b.is_anchor) return 1;
        return a.title.localeCompare(b.title);
      });
      maxRows = Math.max(maxRows, list.length);
      const x = unit ? leftPad + Math.max(0,(columnWidth-nodeWidth)/2) : leftPad + columnIndex*columnWidth + 10;
      list.forEach((node, rowIndex) => {
        const y = 25 + rowIndex*rowGap;
        positions.set(node.id,{x,y,w:nodeWidth,h:nodeHeight,cx:x+nodeWidth/2,cy:y+nodeHeight/2});
      });
    });
    const height = Math.max(500, 60 + maxRows*rowGap);
    return {positions,width,height,nodeWidth,nodeHeight,units};
  }
  function renderGraph() {
    filteredData();
    const svg = $("kg-svg");
    svg.replaceChildren();
    if (!visibleNodes.length) {
      svg.setAttribute("viewBox","0 0 900 450");
      svg.appendChild(el("text",{x:450,y:225,"text-anchor":"middle",fill:"#667487"}, "No concepts match this search."));
      $("kg-count").textContent = "0 concepts";
      return;
    }
    const layout = layoutNodes();
    const query = searchText.trim().toLowerCase();
    const searchMatches = visibleNodes.filter(node => `${node.title} ${node.summary} ${node.explanation} ${node.unit_title}`.toLowerCase().includes(query));
    svg.setAttribute("viewBox",`0 0 ${layout.width} ${layout.height}`);
    svg.setAttribute("preserveAspectRatio","xMinYMin meet");
    const positions = layout.positions;
    const edgeGroup = el("g",{"aria-hidden":"true"});
    visibleEdges.forEach(edge => {
      const a=positions.get(edge.source), b=positions.get(edge.target);
      if (!a || !b) return;
      const unitEdge = edge.kind === "unit";
      let d;
      if (Math.abs(a.cx-b.cx)<8) d=`M ${a.cx} ${a.cy+a.h/2} L ${b.cx} ${b.cy-b.h/2}`;
      else {
        const midX=(a.cx+b.cx)/2;
        d=`M ${a.cx} ${a.cy} C ${midX} ${a.cy}, ${midX} ${b.cy}, ${b.cx} ${b.cy}`;
      }
      const onPath=pathIds.has(edge.source)&&pathIds.has(edge.target);
      edgeGroup.appendChild(el("path",{
        d,fill:"none",stroke:onPath?"#dc7a36":unitEdge?"#c9d6df":"#9fb3c3",
        "stroke-width":onPath?3.6:unitEdge?1.2:1.7,
        "stroke-dasharray":unitEdge?"5 5":"none",
        opacity:(searchText && !onPath)?0.48:0.82
      }));
    });
    svg.appendChild(edgeGroup);
    const nodeGroup=el("g");
    visibleNodes.forEach(node=>{
      const p=positions.get(node.id);
      if (!p) return;
      const isSelected=node.id===selectedId;
      const isPath=pathIds.has(node.id);
      const matches=!searchText || `${node.title} ${node.summary} ${node.unit_title}`.toLowerCase().includes(searchText.trim().toLowerCase());
      const group=el("g",{
        transform:`translate(${p.x},${p.y})`,
        tabindex:"0",role:"button",
        "aria-label":`${node.title}, unit ${node.unit}`,
        "data-node-id":node.id,
        style:"cursor:pointer;outline:none",
        opacity:matches?1:0.23
      });
      const color=UNIT_COLORS[node.unit]||"#287bb5";
      group.appendChild(el("rect",{
        x:0,y:0,width:p.w,height:p.h,rx:node.is_anchor?15:10,
        fill:node.is_anchor?`${color}18`:"#ffffff",
        stroke:isSelected?"#102b43":isPath?"#dc7a36":node.is_anchor?color:"#d5e0e8",
        "stroke-width":isSelected?3:isPath?3:node.is_anchor?1.8:1.2
      }));
      group.appendChild(el("circle",{cx:15,cy:16,r:4.5,fill:color}));
      const title=String(node.title||"");
      const titleMax=node.is_anchor?30:31;
      group.appendChild(el("text",{x:27,y:21,fill:"#172536","font-size":node.is_anchor?11.5:11.2,"font-weight":node.is_anchor?750:700},title.length>titleMax?title.slice(0,titleMax-1)+"…":title));
      const subtitle=node.is_anchor?"UNIT ENTRY POINT":`UNIT ${node.unit} · ${node.is_anchor?"ANCHOR":"LESSON TOPIC"}`;
      group.appendChild(el("text",{x:14,y:40,fill:"#667487","font-size":8.5,"letter-spacing":".4"},subtitle));
      group.addEventListener("click",()=>selectNode(node.id));
      group.addEventListener("keydown",event=>{if(event.key==="Enter"||event.key===" "){event.preventDefault();selectNode(node.id);}});
      nodeGroup.appendChild(group);
    });
    svg.appendChild(nodeGroup);
    $("kg-count").textContent = `${visibleNodes.length} nodes · ${visibleEdges.length} links${query ? ` · ${searchMatches.length} search matches` : ""}`;
  }
  function selectNode(id) {
    const node=allNodes.find(item=>item.id===id);
    if (!node) return;
    selectedId=id;
    $("kg-detail-title").textContent=node.title;
    $("kg-detail-summary").textContent=node.explanation || node.summary || "No expanded explanation is available in the current catalogue.";
    $("kg-detail-meta").innerHTML=`<span>Unit ${node.unit}</span><span>${safeText(node.unit_title)}</span>${node.is_anchor?'<span>Navigation anchor</span>':'<span>Lesson topic</span>'}`;
    const formula=$("kg-detail-formula");
    if(node.formula){formula.hidden=false;formula.textContent=node.formula;}else{formula.hidden=true;formula.textContent="";}
    $("kg-lesson-link").href=node.url || "/syllabus";
    $("kg-lesson-link").textContent=node.is_anchor?"Open syllabus →":"Open lesson →";
    const connections=allEdges.filter(edge=>edge.source===id||edge.target===id).map(edge=>{
      const otherId=edge.source===id?edge.target:edge.source;
      const other=allNodes.find(item=>item.id===otherId);
      return other?{node:other,label:edge.label,kind:edge.kind}:null;
    }).filter(Boolean);
    connections.sort((a,b)=>a.node.unit-b.node.unit||a.node.title.localeCompare(b.node.title));
    $("kg-related").innerHTML=connections.length?connections.map(item=>`<li><button type="button" data-related="${safeText(item.node.id)}"><span>${safeText(item.node.title)}</span><small>${safeText(item.label)} · Unit ${item.node.unit}</small></button></li>`).join(""):'<li>No connected concepts in the current catalogue.</li>';
    $("kg-related").querySelectorAll("[data-related]").forEach(button=>button.addEventListener("click",()=>{const target=button.getAttribute("data-related");const node=allNodes.find(n=>n.id===target);if(node&&Number($("kg-unit").value)&&node.unit!==Number($("kg-unit").value))$("kg-unit").value="0";renderGraph();selectNode(target);}));
    if(!visibleNodes.some(item=>item.id===id)) {
      if(node.unit) $("kg-unit").value=String(node.unit);
      $("kg-search").value="";
      searchText="";
      renderGraph();
    } else renderGraph();
    $("kg-from").value=allNodes.some(item=>item.id===$("kg-from").value)?$("kg-from").value:id;
    $("kg-to").value=allNodes.some(item=>item.id===$("kg-to").value)?$("kg-to").value:id;
  }
  function fillPathSelects() {
    const topics=allNodes.filter(node=>!node.is_anchor);
    const options=topics.map(node=>`<option value="${safeText(node.id)}">${safeText(node.title)} · Unit ${node.unit}</option>`).join("");
    $("kg-from").innerHTML=options;
    $("kg-to").innerHTML=options;
    if(topics.length>1)$("kg-to").selectedIndex=1;
  }
  async function findPath() {
    const from=$("kg-from").value,to=$("kg-to").value;
    const box=$("kg-path-result");
    box.textContent="Finding a route…";
    try {
      const response=await fetch(`/graph/path?from=${encodeURIComponent(from)}&to=${encodeURIComponent(to)}`,{headers:{"Accept":"application/json"}});
      const result=await response.json();
      if(!response.ok||!result.ok)throw new Error(result.error||"Could not find a route.");
      pathIds=new Set(result.path.map(node=>node.id));
      box.innerHTML=`<strong>${result.path.length} nodes in the suggested route</strong><ol>${result.path.map(node=>`<li><button type="button" data-path-node="${safeText(node.id)}">${safeText(node.title)} <small>Unit ${node.unit}</small></button></li>`).join("")}</ol><p>Routes follow navigation links and may cross unit anchors. Treat them as study suggestions, not mandatory prerequisites.</p>`;
      box.querySelectorAll("[data-path-node]").forEach(button=>button.addEventListener("click",()=>{
        const id=button.getAttribute("data-path-node");
        const node=allNodes.find(item=>item.id===id);
        if(node&&!node.is_anchor&&Number($("kg-unit").value)&&node.unit!==Number($("kg-unit").value))$("kg-unit").value="0";
        $("kg-search").value="";searchText="";renderGraph();selectNode(id);
      }));
      if(Number($("kg-unit").value))$("kg-unit").value="0";
      $("kg-search").value="";searchText="";
      renderGraph();
    } catch(error) {
      pathIds.clear();
      box.textContent=error.message;
      renderGraph();
    }
  }
  $("kg-search").addEventListener("input",()=>{searchText=$("kg-search").value;renderGraph();});
  $("kg-unit").addEventListener("change",()=>{renderGraph();});
  $("kg-fit").addEventListener("click",()=>{renderGraph();$("kg-canvas-wrap").scrollTo({left:0,top:0,behavior:"smooth"});});
  $("kg-clear").addEventListener("click",()=>{selectedId=null;pathIds.clear();$("kg-detail-title").textContent="Choose a topic";$("kg-detail-summary").textContent="Select any node in the map to see its unit, short explanation, formula (when available), and connected topics.";$("kg-detail-meta").replaceChildren();$("kg-detail-formula").hidden=true;$("kg-related").innerHTML="<li>Connections will appear here.</li>";$("kg-lesson-link").href="/learn/";$("kg-search").value="";searchText="";renderGraph();});
  $("kg-find-path").addEventListener("click",findPath);
  window.addEventListener("resize",()=>renderGraph());
  loadGraph();
})();