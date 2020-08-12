function CopyAddresslistValuesToClipboard()
  local al=getAddressList()
  local values=""
  for i=0, al.Count-1 do
    values=values..al[i].Value.."#"
  end
  writeToClipboard(values)
end

copytimer=createTimer(nil)
copytimer.OnTimer=CopyAddresslistValuesToClipboard
copytimer.Interval=100
