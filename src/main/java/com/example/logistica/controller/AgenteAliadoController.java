package com.example.logistica.controller;

import com.example.logistica.entity.AgenteAliado;
import com.example.logistica.service.AgenteAliadoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/agentes")
public class AgenteAliadoController {

    private final AgenteAliadoService agenteService;

    public AgenteAliadoController(AgenteAliadoService agenteService) {
        this.agenteService = agenteService;
    }

    @PostMapping("/")
    public ResponseEntity<AgenteAliado> registrarAgente(@RequestBody AgenteAliado agente) {
        return ResponseEntity.ok(agenteService.registrarAgente(agente));
    }

    @GetMapping("/{id}")
    public ResponseEntity<AgenteAliado> consultarAgente(@PathVariable Long id) {
        return ResponseEntity.ok(agenteService.consultarAgente(id));
    }

    @GetMapping("/")
    public ResponseEntity<List<AgenteAliado>> consultarAgentes() {
        return ResponseEntity.ok(agenteService.consultarAgentes());
    }

    @PatchMapping("/{id}/almacen/{idAlmacen}")
    public ResponseEntity<AgenteAliado> asignarAlmacen(@PathVariable Long id, @PathVariable Long idAlmacen){
        return ResponseEntity.ok(agenteService.asignarAlmacen(id, idAlmacen));
    }

    @PatchMapping("/{id}/conductor/{idConductor}")
    public ResponseEntity<AgenteAliado> asignarConductorAagente(@PathVariable Long id, @PathVariable Long idConductor){
        return ResponseEntity.ok(agenteService.asignarConductorAagente(id, idConductor));
    }
}
